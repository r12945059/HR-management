# HR-management (API + Docker)

## Features
- View employees
- Add / Edit / Delete employees
- Bulk upload via Excel (.xlsx / .xls)
- Single Dockerized service

## Quick Start
```bash
docker build -t hrms-api .
docker run --name hrms-api -p 8000:8000 hrms-api
# optional: persist SQLite
# docker run --name hrms-api -p 8000:8000 -v "$(pwd)/hr.db:/app/hr.db" hrms-api
