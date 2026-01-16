from fastapi import APIRouter, HTTPException, Body, Query
from services.ai_service import AIService
from services.file_service import FileService
from services.eda_service import EDAService
from models.schemas import ReportRequest

router = APIRouter()

@router.post("/report/generate")
async def generate_report(
    file_id: str = Query(...),
    filename: str = Query(...),
    format: str = Query("html", regex="^(html|pdf)$")
):
    """Generate AI-powered report"""
    try:
        df = FileService.load_dataframe(file_id, filename)
        summary = EDAService.get_summary(df)
        
        # Generate AI report
        report_result = await AIService.generate_report(str(summary))
        
        return {
            "report": report_result.get("report"),
            "format": format,
            "status": report_result.get("status", "error")
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
