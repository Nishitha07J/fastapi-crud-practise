# FastAPI CRUD API with PostgreSQL

A practice project built while learning FastAPI. This REST API performs CRUD operations using FastAPI and PostgreSQL, with pgAdmin used to manage the database.

## Features

- CRUD operations
- RESTful API endpoints
- PostgreSQL database integration
- SQLAlchemy ORM
- Request and response validation with Pydantic
- Automatic API documentation (Swagger UI & ReDoc)

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn
- pgAdmin (Database GUI)

## Prerequisites

- Python 3.11+
- PostgreSQL
- pgAdmin (optional, for database management)

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-postgres-crud.git
cd fastapi-postgres-crud
```

2. Create and activate a virtual environment

```bash
python -m venv .venv
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure your database connection.

Create a `.env` file (or update the connection string in your configuration):

```env
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```

5. Run the application

```bash
uvicorn main:app --reload
```

## API Documentation

Once the server is running:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Project Structure

```text
.
├── app/
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routers/
│   └── main.py
├── requirements.txt
└── README.md
```

## What I Learned

- Building REST APIs with FastAPI
- Creating CRUD endpoints
- Connecting FastAPI to PostgreSQL
- Using SQLAlchemy for database operations
- Data validation with Pydantic
- Managing a PostgreSQL database with pgAdmin
- Organizing a FastAPI project into modules

## Disclaimer

This project was created as part of my FastAPI learning journey and is intended for educational purposes.
