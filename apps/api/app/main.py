from fastapi import FastAPI

from app.core.config import get_settings
from app.db.session import check_database_connection

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="Backend API for the ClinicFlow scheduling platform.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    database_ok = check_database_connection()

    return {
        "status": "ok",
        "environment": settings.app_env,
        "runtime_mode": settings.runtime_mode,
        "database": "ok" if database_ok else "unavailable",
    }