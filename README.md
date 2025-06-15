# FastAPI Example Project

This is a FastAPI-based REST API project with a clean architecture.

## Features

- FastAPI framework
- SQLAlchemy ORM
- Pydantic data validation
- JWT Authentication
- Database migrations with Alembic
- Unit tests with pytest
- Clean architecture

## Project Structure

```
project_name/
├── app/
│   ├── main.py         # Main application entry point
│   ├── routes/         # API endpoint definitions
│   ├── models/         # SQLAlchemy models
│   ├── services/       # Business logic
│   ├── utils/          # Utility functions
│   ├── config/         # Configuration settings
│   └── middleware/     # Custom middleware
├── tests/              # Test files
├── migrations/         # Database migrations
└── docs/              # Documentation
```

## Getting Started

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate   # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file and set your environment variables
5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Documentation

Once the application is running, you can access:
- API documentation at `/docs`
- Alternative API documentation at `/redoc`

## Testing

Run tests with pytest:
```bash
pytest
```
