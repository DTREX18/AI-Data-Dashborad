from fastapi import APIRouter, HTTPException, Query, Body
from services.ml_service import MLService
from services.file_service import FileService
from models.schemas import ModelTraining, ModelMetrics

router = APIRouter()

@router.post("/model/train")
async def train_model(
    file_id: str = Query(...),
    filename: str = Query(...),
    training_config: ModelTraining = Body(...)
):
    """Train ML model"""
    try:
        df = FileService.load_dataframe(file_id, filename)
        
        if training_config.model_type == "regression":
            result = MLService.train_regression_model(
                df,
                training_config.target_column,
                "linear"
            )
        elif training_config.model_type == "classification":
            result = MLService.train_classification_model(
                df,
                training_config.target_column
            )
        else:
            raise HTTPException(status_code=400, detail="Invalid model type")
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
