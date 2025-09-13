from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional, List
import pandas as pd
import io

app = FastAPI(title="HRMS", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    department: Optional[str] = None
    title: Optional[str] = None
    hire_date: Optional[str] = None
    salary: Optional[float] = None

sqlite_url = "sqlite:///./hr.db"
engine = create_engine(sqlite_url, echo=False)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/employees", response_model=List[Employee])
def list_employees():
    with Session(engine) as s:
        return s.exec(select(Employee)).all()

@app.post("/employees", response_model=Employee)
def create_employee(emp: Employee):
    with Session(engine) as s:
        s.add(emp); s.commit(); s.refresh(emp); return emp

@app.put("/employees/{emp_id}", response_model=Employee)
def update_employee(emp_id: int, data: Employee):
    with Session(engine) as s:
        obj = s.get(Employee, emp_id)
        if not obj: raise HTTPException(404, "Not found")
        for k, v in data.dict(exclude_unset=True).items():
            setattr(obj, k, v)
        s.add(obj); s.commit(); s.refresh(obj); return obj

@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    with Session(engine) as s:
        obj = s.get(Employee, emp_id)
        if not obj: raise HTTPException(404, "Not found")
        s.delete(obj); s.commit(); return {"ok": True}

@app.post("/employees/upload")
async def bulk_upload(file: UploadFile = File(...)):
    if not file.filename.lower().endswith((".xlsx", ".xls")):
        raise HTTPException(400, "Please upload an Excel file")
    content = await file.read()
    df = pd.read_excel(io.BytesIO(content))
    required = {"first_name","last_name","email"}
    if not required.issubset(df.columns.str.lower()):
        raise HTTPException(400, f"Excel must include columns: {sorted(required)}")

    df.columns = [c.strip().lower() for c in df.columns]
    rows = df.to_dict(orient="records")
    with Session(engine) as s:
        for r in rows:
            s.add(Employee(**{k: r.get(k) for k in Employee.__fields__.keys() if k in r}))
        s.commit()
    return {"inserted": len(rows)}
