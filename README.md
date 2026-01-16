# AI Data Analytics Dashboard

A full-stack AI-powered data analytics platform with predictive modeling, forecasting, risk assessment, and intelligent insights.

## Features

- **Dataset Upload**: Support for CSV and XLSX files
- **Exploratory Data Analysis (EDA)**: Automatic data profiling and statistics
- **Predictive Analytics**: ML models (Linear Regression, Random Forest)
- **Time Series Forecasting**: Prophet-based demand prediction
- **Risk Assessment**: Anomaly detection and risk scoring
- **AI Insights**: Chat with your data using OpenRouter AI models
- **Report Generation**: PDF/HTML automated reports

## Tech Stack

### Frontend
- Next.js 14 (App Router)
- React 19
- TypeScript
- TailwindCSS v4
- Recharts for visualizations
- Shadcn/ui components

### Backend
- Python FastAPI
- Pandas, NumPy for data processing
- Scikit-learn for ML
- Prophet for time series forecasting
- YData Profiling for data profiling

### Database & Storage
- Supabase (PostgreSQL + Storage)
- Or SQLite for local development

### AI
- OpenRouter.com for LLM access
- Models: deepseek-r1, qwen2.5-72b, llama-3.1-70b

## Prerequisites

- Node.js 18+
- Python 3.9+
- npm or yarn
- OpenRouter API key
- Supabase account (optional)

## Setup Instructions

### Frontend Setup

```bash
# Install dependencies
npm install

# Create environment variables
cp .env.example .env.local

# Update .env.local with your values
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_OPENROUTER_API_KEY=your_key_here
```

```bash
# Run development server
npm run dev

# Visit http://localhost:3000
```

### Backend Setup

```bash
# Create Python virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\\Scripts\\activate

# Install dependencies
pip install fastapi uvicorn pandas numpy scikit-learn prophet ydata-profiling python-multipart

# Create .env file
cp backend/.env.example backend/.env

# Update with your OpenRouter API key and Supabase credentials
```

```bash
# Run FastAPI server
cd backend
uvicorn main:app --reload --port 8000

# API docs available at http://localhost:8000/docs
```

## Environment Variables

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_OPENROUTER_API_KEY=your_openrouter_key
```

### Backend (.env)
```
OPENROUTER_API_KEY=your_openrouter_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
DATABASE_URL=postgresql://...
```

## API Endpoints

- `POST /upload` - Upload dataset
- `GET /eda/summary` - EDA summary statistics
- `GET /eda/charts` - Chart-ready data
- `POST /model/train` - Train ML model
- `POST /forecast` - Time series forecasting
- `POST /risk/analyze` - Anomaly detection
- `POST /ai/chat` - AI Q&A using OpenRouter
- `POST /report/generate` - Generate AI report

## Deployment

### Deploy Frontend to Vercel
```bash
npm install -g vercel
vercel
```

### Deploy Backend to Railway
```bash
# Create Railway account and project
railway init
railway up
```

## Project Structure

```
.
├── app/                    # Next.js app directory
├── components/             # React components
│   ├── dashboard.tsx       # Main dashboard
│   ├── sidebar.tsx         # Navigation sidebar
│   ├── data-uploader.tsx   # File upload component
│   └── tabs/               # Tab components for each section
├── lib/                    # Utility functions
├── backend/                # FastAPI backend
│   ├── main.py            # Entry point
│   ├── routes/            # API routes
│   ├── services/          # Business logic
│   └── models/            # Pydantic models
└── scripts/               # Database setup scripts
```

## License

MIT

## Support

For issues or questions, please open a GitHub issue or contact support.
# AI-Data-Dashborad
