from fastapi import APIRouter, HTTPException, Query
from services.risk_service import RiskService
from services.file_service import FileService

router = APIRouter()

@router.post("/risk/analyze")
async def analyze_risk(
    file_id: str = Query(...),
    filename: str = Query(...),
    contamination: float = Query(0.1, ge=0.01, le=0.5)
):
    """Detect anomalies and calculate risk"""
    try:
        df = FileService.load_dataframe(file_id, filename)
        result = RiskService.detect_anomalies(df, contamination)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/risk/quality")
async def get_data_quality(file_id: str = Query(...), filename: str = Query(...)):
    """Get data quality score"""
    try:
        df = FileService.load_dataframe(file_id, filename)
        score = RiskService.get_data_quality_score(df)
        return {"quality_score": score}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
