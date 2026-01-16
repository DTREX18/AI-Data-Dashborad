from fastapi import APIRouter, HTTPException, Query
from services.eda_service import EDAService
from services.file_service import FileService
import pandas as pd

router = APIRouter()

@router.get("/eda/summary")
async def get_eda_summary(file_id: str = Query(...), filename: str = Query(...)):
    """Get EDA summary for dataset"""
    try:
        df = FileService.load_dataframe(file_id, filename)
        summary = EDAService.get_summary(df)
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/eda/stats")
async def get_column_stats(file_id: str = Query(...), filename: str = Query(...)):
    """Get column statistics"""
    try:
        df = FileService.load_dataframe(file_id, filename)
        stats = EDAService.get_column_stats(df)
        return stats
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/eda/correlation")
async def get_correlation(file_id: str = Query(...), filename: str = Query(...)):
    """Get correlation matrix"""
    try:
        df = FileService.load_dataframe(file_id, filename)
        correlation = EDAService.get_correlation_matrix(df)
        return correlation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/eda/outliers")
async def get_outliers(file_id: str = Query(...), filename: str = Query(...)):
    """Detect outliers"""
    try:
        df = FileService.load_dataframe(file_id, filename)
        outliers = EDAService.get_outliers(df)
        return outliers
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/eda/charts")
async def get_chart_data(file_id: str = Query(...), filename: str = Query(...)):
    """Get chart-ready data"""
    try:
        df = FileService.load_dataframe(file_id, filename)
        charts = EDAService.get_chart_data(df)
        return {"charts": charts}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
