from fastapi import APIRouter, HTTPException, Query, Body
from services.forecast_service import ForecastService
from services.file_service import FileService
from models.schemas import ForecastRequest

router = APIRouter()

@router.post("/forecast")
async def forecast(
    file_id: str = Query(...),
    filename: str = Query(...),
    config: ForecastRequest = Body(...)
):
    """Generate time series forecast"""
    try:
        df = FileService.load_dataframe(file_id, filename)
        
        result = ForecastService.forecast_time_series(
            df,
            config.date_column,
            config.value_column,
            config.periods
        )
        
        if "error" in result:
            # Fallback to simple forecast
            result = ForecastService.simple_forecast(
                df,
                config.value_column,
                config.periods
            )
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
