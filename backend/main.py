from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="AI Data Analytics Dashboard API",
    description="Backend API for data analytics, ML, and AI insights",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import routes
from routes import upload, eda, models, forecast, risk, ai_insights, reports

# Include routers
app.include_router(upload.router, prefix="/api", tags=["Upload"])
app.include_router(eda.router, prefix="/api", tags=["EDA"])
app.include_router(models.router, prefix="/api", tags=["Models"])
app.include_router(forecast.router, prefix="/api", tags=["Forecast"])
app.include_router(risk.router, prefix="/api", tags=["Risk"])
app.include_router(ai_insights.router, prefix="/api", tags=["AI Insights"])
app.include_router(reports.router, prefix="/api", tags=["Reports"])

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "AI Data Analytics Dashboard API",
        "docs": "/docs",
        "health": "ok"
    }

# Health check
@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
