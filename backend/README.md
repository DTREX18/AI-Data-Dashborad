# FastAPI Backend

## Setup

```bash
# Create virtual environment
python -m venv venv

# Activate
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Update .env with your OpenRouter API key
```

## Running

```bash
uvicorn main:app --reload --port 8000
```

Visit `http://localhost:8000/docs` for API documentation.

## Endpoints

- `POST /api/upload` - Upload dataset
- `GET /api/eda/summary` - EDA summary
- `GET /api/eda/stats` - Column statistics
- `GET /api/eda/correlation` - Correlation matrix
- `GET /api/eda/outliers` - Outlier detection
- `GET /api/eda/charts` - Chart data
- `POST /api/model/train` - Train ML model
- `POST /api/forecast` - Time series forecasting
- `POST /api/risk/analyze` - Anomaly detection
- `GET /api/risk/quality` - Data quality score
- `POST /api/ai/chat` - Chat with data
- `POST /api/report/generate` - Generate report
