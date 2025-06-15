# FastAPI Example Project

A modern, clean-architecture REST API project using FastAPI, SQLAlchemy, and PostgreSQL.

## Features

- FastAPI framework
- SQLAlchemy ORM
- Pydantic data validation
- JWT Authentication
- Database migrations with Alembic
- Unit tests with pytest
- PostgreSQL support (Docker-ready)
- Clean, modular architecture
- Custom exception handling
- Swagger UI & ReDoc API docs

## Project Structure

```
project_name/
├── app/
│   ├── main.py           # Main application entry point
│   ├── controllers/      # Class-based controllers
│   ├── routes/           # API endpoint definitions
│   ├── models/           # SQLAlchemy models
│   ├── services/         # Business logic
│   ├── utils/            # Utility functions & exceptions
│   ├── config/           # Configuration settings
│   ├── middleware/       # Custom middleware
├── tests/                # Test files
├── migrations/           # Database migrations
├── docs/                 # Documentation
├── scripts/              # Helper scripts
├── logs/                 # Log files
├── requirements.txt      # Project dependencies
├── docker-compose.yaml   # Docker Compose for local dev
├── Dockerfile            # Docker build config
└── README.md             # Project documentation
```

## Getting Started

1. **Clone the repository**
2. **Create a virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
4. **Configure environment variables:**
   - Copy `.env.dev` to `.env` and adjust as needed
5. **Run the application:**
   ```powershell
   uvicorn app.main:app --reload
   ```

Or use Docker Compose:
```powershell
docker-compose up --build
```

## API Documentation

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Testing

Run all tests with pytest:
```powershell
pytest
```

## Migrations

Create and apply database migrations with Alembic:
```powershell
alembic revision --autogenerate -m "Your message"
alembic upgrade head
```

## Exception Handling

Custom exceptions (e.g. `NotFoundException`) are globally handled and return JSON responses with status code and message.

## License

MIT License
