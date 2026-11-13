# Task Management API 🚀

A RESTful Task Management API built using **FastAPI, SQLAlchemy, and MySQL**. This project focuses on building a scalable backend application with database integration and structured API development.

## 🛠️ Tech Stack

- **Language:** Python
- **Backend Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Database:** MySQL
- **Database Driver:** PyMySQL
- **Configuration Management:** Pydantic Settings
- **Database Migrations:** Alembic (Planned / In Progress)

## 📌 Current Features

- FastAPI application setup
- Modular project structure using Python packages
- MySQL database connectivity
- SQLAlchemy ORM integration
- Task model and database table creation
- Environment variable management using Pydantic Settings
- Basic task creation functionality

## 📂 Project Structure

```text
Task-Management-API/
│
├── src/
│   ├── task/
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── schemas.py
│   │
│   └── utils/
│       ├── db.py
│       └── config.py
│
├── main.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

*Note: The project structure may evolve as development progresses.*

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Task-Management-API.git
cd Task-Management-API
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root using `.env.example`.

Configure your MySQL connection:

```env
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/fastapi_db
```

### 5. Create the MySQL database

```sql
CREATE DATABASE fastapi_db;
```

### 6. Run the application

```bash
fastapi dev main.py
```

## 📖 API Documentation

Once the application is running, access the interactive API documentation:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## 🚧 Upcoming Improvements

- Complete CRUD operations for tasks
- Alembic database migrations
- User authentication and authorization using JWT
- Pagination and filtering
- Improved error handling and validation
- Docker integration
- Cloud deployment

## 🎯 Project Goal

The goal of this project is to develop a structured, maintainable, and scalable backend application while gaining practical experience with REST APIs, relational databases, ORM-based database operations, and backend development.

---

**Status:** 🚧 Under Active Development
