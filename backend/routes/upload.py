from fastapi import APIRouter, UploadFile, File, HTTPException
from services.file_service import FileService
from models.schemas import FileUploadResponse
import json

router = APIRouter()

@router.post("/upload", response_model=FileUploadResponse)
async def upload_dataset(file: UploadFile = File(...)):
    """Upload dataset file"""
    try:
        content = await file.read()
        
        # Validate file
        is_valid, message = FileService.validate_file(file.filename, len(content))
        if not is_valid:
            raise HTTPException(status_code=400, detail=message)
        
        # Save file
        file_id = FileService.save_file(content, file.filename)
        
        # Load and analyze
        df = FileService.load_dataframe(file_id, file.filename)
        file_info = FileService.get_file_info(df, file_id, file.filename)
        
        return FileUploadResponse(**file_info)
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
