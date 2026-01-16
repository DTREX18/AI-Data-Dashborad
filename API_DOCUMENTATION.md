# API Documentation

## Base URL

Development: `http://localhost:8000`
Production: `https://your-backend-url.railway.app`

## Authentication

All requests should include headers:
```
Content-Type: application/json
Authorization: Bearer your_openrouter_key (for AI endpoints)
```

## Endpoints

### File Upload

**POST /api/upload**

Upload a dataset file.

Request:
```bash
curl -X POST -F "file=@data.csv" http://localhost:8000/api/upload
```

Response:
```json
{
  "id": "file-123",
  "filename": "data.csv",
  "size": 1024,
  "rows": 100,
  "columns": 5,
  "column_names": ["name", "age", "salary", "department", "date"],
  "upload_time": "2024-01-16T12:00:00"
}
```

### EDA Endpoints

**GET /api/eda/summary**

Get dataset summary statistics.

Parameters:
- `file_id` (required): File ID from upload
- `filename` (required): Original filename

Response:
```json
{
  "row_count": 1000,
  "column_count": 5,
  "memory_usage": "0.05 MB",
  "missing_values": {"name": 0, "age": 2, "salary": 1},
  "data_types": {"name": "object", "age": "int64"},
  "numeric_summary": {"age": {"mean": 35.5, "std": 10.2}}
}
```

**GET /api/eda/stats**

Get column statistics.

**GET /api/eda/correlation**

Get correlation matrix.

**GET /api/eda/outliers**

Detect outliers.

**GET /api/eda/charts**

Get chart data.

### Model Endpoints

**POST /api/model/train**

Train ML model.

Request:
```json
{
  "target_column": "salary",
  "model_type": "regression",
  "features": ["age", "experience"]
}
```

Response:
```json
{
  "model_type": "regression",
  "target": "salary",
  "r_squared": 0.87,
  "rmse": 5234.2,
  "mae": 3421.5,
  "samples_trained": 800
}
```

### Forecast Endpoints

**POST /api/forecast**

Generate time series forecast.

Request:
```json
{
  "date_column": "date",
  "value_column": "sales",
  "periods": 12
}
```

Response:
```json
{
  "forecast": [
    {"ds": "2024-02-01", "yhat": 5234.2},
    {"ds": "2024-02-02", "yhat": 5340.1}
  ],
  "lower_bound": [5100, 5200],
  "upper_bound": [5300, 5400],
  "periods": 12
}
```

### Risk Endpoints

**POST /api/risk/analyze**

Detect anomalies.

Parameters:
- `file_id` (required)
- `filename` (required)
- `contamination` (optional, default: 0.1)

Response:
```json
{
  "anomalies": [
    {"row_index": 5, "value": 99999, "deviation": 5.2}
  ],
  "total_anomalies": 10,
  "risk_score": 1.0,
  "summary": "Detected 10 anomalies (1.0% of data)"
}
```

**GET /api/risk/quality**

Get data quality score.

Response:
```json
{
  "quality_score": 94.5
}
```

### AI Endpoints

**POST /api/ai/chat**

Chat with your data.

Request:
```json
{
  "question": "What are the main trends?",
  "context": "Dataset summary here..."
}
```

Response:
```json
{
  "answer": "Based on the data, the main trends show...",
  "confidence": 0.92
}
```

### Report Endpoints

**POST /api/report/generate**

Generate AI report.

Parameters:
- `file_id` (required)
- `filename` (required)
- `format` (optional, default: "html")

Response:
```json
{
  "report": "<html>...",
  "format": "html",
  "status": "success"
}
```

## Error Responses

All errors follow this format:

```json
{
  "detail": "Error message here"
}
```

Common HTTP Status Codes:
- `200`: Success
- `400`: Bad request (invalid parameters)
- `401`: Unauthorized
- `404`: Not found
- `500`: Server error
- `413`: File too large

## Rate Limiting

- File uploads: 10/minute
- API calls: 100/minute
- AI queries: 30/minute (OpenRouter limit)

## Examples

### Python
```python
import requests

# Upload file
files = {'file': open('data.csv', 'rb')}
response = requests.post('http://localhost:8000/api/upload', files=files)
file_data = response.json()

# Get summary
params = {
    'file_id': file_data['id'],
    'filename': file_data['filename']
}
summary = requests.get('http://localhost:8000/api/eda/summary', params=params).json()
print(summary)
```

### JavaScript
```javascript
// Upload file
const formData = new FormData();
formData.append('file', fileInput.files[0]);

const response = await fetch('http://localhost:8000/api/upload', {
  method: 'POST',
  body: formData
});

const fileData = await response.json();

// Get summary
const summary = await fetch(
  `/api/eda/summary?file_id=${fileData.id}&filename=${fileData.filename}`
).then(r => r.json());
```

### cURL
```bash
# Upload
curl -X POST -F "file=@data.csv" http://localhost:8000/api/upload

# Get summary
curl "http://localhost:8000/api/eda/summary?file_id=abc123&filename=data.csv"

# Chat
curl -X POST http://localhost:8000/api/ai/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"What are trends?","context":"..."}'
