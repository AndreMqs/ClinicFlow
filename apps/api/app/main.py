from fastapi import FastAPI

app = FastAPI(
    title="ClinicFlow API",
    description="Backend API for the ClinicFlow scheduling platform.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}