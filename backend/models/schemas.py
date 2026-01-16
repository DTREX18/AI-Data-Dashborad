from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class FileUploadResponse(BaseModel):
    id: str
    filename: str
    size: int
    rows: int
    columns: int
    column_names: List[str]
    upload_time: str

class EdaSummary(BaseModel):
    row_count: int
    column_count: int
    memory_usage: str
    missing_values: Dict[str, int]
    data_types: Dict[str, str]
    numeric_summary: Dict[str, Dict[str, float]]

class ChartData(BaseModel):
    name: str
    type: str
    data: List[Dict[str, Any]]

class ModelTraining(BaseModel):
    target_column: str
    model_type: str  # "regression" or "classification"
    features: Optional[List[str]] = None

class ModelMetrics(BaseModel):
    model_type: str
    accuracy: Optional[float] = None
    r_squared: Optional[float] = None
    rmse: Optional[float] = None
    mae: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None

class ForecastRequest(BaseModel):
    date_column: str
    value_column: str
    periods: int = 12

class ForecastResponse(BaseModel):
    forecast: List[Dict[str, Any]]
    lower_bound: List[float]
    upper_bound: List[float]

class AnomalyDetectionResult(BaseModel):
    anomalies: List[Dict[str, Any]]
    risk_score: float
    summary: str

class ChatMessage(BaseModel):
    question: str
    context: Optional[str] = None

class AIResponse(BaseModel):
    answer: str
    confidence: float
    sources: Optional[List[str]] = None

class ReportRequest(BaseModel):
    dataset_id: str
    format: str  # "pdf" or "html"
    sections: List[str]
