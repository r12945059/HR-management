# HR-management (FastAPI + Docker)

簡易的人資管理平台，提供員工清單瀏覽、建立/編輯/刪除、以及 Excel 批次上傳。已容器化，支援一鍵建置與執行。

---

## Features
- View employees（查看員工清單）
- Add / Edit / Delete employees（新增 / 編輯 / 刪除）
- Bulk upload via Excel（支援 .xlsx / .xls 批次上傳）
- Single Dockerized service（單一 Docker 服務）

---

## Quick Start

```bash
# 於專案根目錄（含 Dockerfile）建置映像檔
docker build -t hrms-api .

# 執行容器（將主機的 8000 對應到容器的 8000）
docker run --name hrms-api -p 8000:8000 hrms-api

# 讓 SQLite 資料庫持久化到主機檔案
# docker run --name hrms-api -p 8000:8000 -v "$(pwd)/hr.db:/app/hr.db" hrms-api
