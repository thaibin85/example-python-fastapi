import uvicorn
import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.config.settings import settings
from app.urls import url_registry
from app.database import engine, Base
from app.utils.exception import BaseException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def create_app() -> FastAPI:
    """Create and configure the FastAPI application"""
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        debug=settings.DEBUG,
        docs_url="/docs",           # Swagger UI
        redoc_url="/redoc",         # ReDoc
        openapi_url="/openapi.json" # OpenAPI schema
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Set up all routes from the URL registry
    url_registry.setup_routes(app)

    @app.on_event("startup")
    async def startup_event():
        logger.info("Starting up the application...")
        # Create database tables
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created")

    @app.on_event("shutdown")
    async def shutdown_event():
        logger.info("Shutting down the application...")

    @app.get("/")
    async def root():
        return {
            "message": "Welcome to FastAPI Example API",
            "version": settings.APP_VERSION,
            "docs_url": "/docs"
        }

    return app

app = create_app()

@app.exception_handler(BaseException)
async def base_exception_handler(request: Request, exc: BaseException):
    return JSONResponse(
        status_code=getattr(exc, "status_code", 400),
        content={"message": getattr(exc, "message", str(exc))}
    )

def main():
    """Main function to run the application"""
    try:
        logger.info("Starting the server...")
        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
    except Exception as e:
        logger.error(f"Error starting server: {e}")
        raise

if __name__ == "__main__":
    main()
