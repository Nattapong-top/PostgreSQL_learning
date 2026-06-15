# Mini Hospital PostgreSQL & Python

โปรเจกต์สำหรับฝึกการพัฒนา Backend ด้วย Python และ PostgreSQL

## Architecture

- Repository Pattern
- Domain Model
- PostgreSQL
---

# Tech Stack

- Python 3.x
- PostgreSQL
- psycopg2
- Pydantic
- Docker
- Ruff
- Black
- mypy

---

# Project Structure

```
mini_hospital_pg_&_py/

├── database/
│
├── src/
│   ├── domain/
│   ├── repository/
│   └── main.py
│
├── .env
├── docker-compose.yml
├── Makefile
└── README.md
```

---

# Current Features

## Patient

- Create Patient
- Find Patient by ID
- Update Patient
- Delete Patient
- Select All Patients

---

## Queue

- Create Queue
- Find Queue by ID
- Update Queue
- Delete Queue
- Select All Queues

---

# Design

```
Application

↓

Repository

↓

PostgreSQL

↓

Row Data

↓

Map To Entity

↓

Domain Entity
```

Repository รับผิดชอบเฉพาะการเข้าถึงข้อมูล

---

# Code Quality

ตรวจสอบคุณภาพโค้ดด้วย

```bash
make check
```

ผลลัพธ์

```
ruff check .
black --check .
mypy .
```

---

# Run PostgreSQL

```bash
docker compose up -d
```

---

# Run Program

```bash
python src/main.py

```

---

# Learning Topics

- Repository Pattern
- Domain Model
- Value Object
- Entity Mapping
- PostgreSQL
- psycopg2
- SQL CRUD
- Context Manager
- Static Type Checking (mypy)

---

# Goal

โปรเจกต์นี้สร้างขึ้นเพื่อศึกษา

- Repository Pattern
- Backend Development with PostgreSQL
