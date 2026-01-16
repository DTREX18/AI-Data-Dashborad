import pandas as pd
import os
from typing import Optional, Tuple
import json
from datetime import datetime
from config import UPLOAD_DIR, MAX_FILE_SIZE, ALLOWED_EXTENSIONS
import uuid

class FileService:
    @staticmethod
    def validate_file(filename: str, size: int) -> Tuple[bool, str]:
        """Validate uploaded file"""
        if size > MAX_FILE_SIZE:
            return False, f"File size exceeds {MAX_FILE_SIZE} bytes"
        
        ext = filename.split(".")[-1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            return False, f"File type not allowed. Allowed: {ALLOWED_EXTENSIONS}"
        
        return True, "valid"
    
    @staticmethod
    def save_file(file_content: bytes, filename: str) -> str:
        """Save uploaded file and return file ID"""
        os.makedirs(UPLOAD_DIR, exist_ok=True)
        file_id = str(uuid.uuid4())
        file_path = os.path.join(UPLOAD_DIR, f"{file_id}_{filename}")
        
        with open(file_path, "wb") as f:
            f.write(file_content)
        
        return file_id
    
    @staticmethod
    def load_dataframe(file_id: str, filename: str) -> pd.DataFrame:
        """Load uploaded file as DataFrame"""
        file_path = os.path.join(UPLOAD_DIR, f"{file_id}_{filename}")
        
        if filename.endswith(".csv"):
            return pd.read_csv(file_path)
        elif filename.endswith(".xlsx"):
            return pd.read_excel(file_path)
        else:
            raise ValueError(f"Unsupported file format: {filename}")
    
    @staticmethod
    def get_file_info(df: pd.DataFrame, file_id: str, filename: str) -> dict:
        """Extract file information"""
        return {
            "id": file_id,
            "filename": filename,
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": df.columns.tolist(),
            "upload_time": datetime.now().isoformat()
        }
