# Development Guide

## Setup

### Frontend

```bash
# Install dependencies
npm install

# Create environment file
cp .env.example .env.local

# Update with your values
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_OPENROUTER_API_KEY=your_key_here

# Run development server
npm run dev
```

Visit http://localhost:3000

### Backend

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Update with your keys
OPENROUTER_API_KEY=your_key_here

# Run development server
python -m uvicorn main:app --reload --port 8000
```

API docs available at http://localhost:8000/docs

## Architecture

### Frontend Structure
```
app/
├── page.tsx              # Home page
├── layout.tsx            # Root layout
└── globals.css           # Global styles

components/
├── dashboard.tsx         # Main dashboard
├── sidebar.tsx           # Navigation
├── header.tsx            # Header
├── data-uploader.tsx     # File upload
├── tab-content.tsx       # Tab router
└── tabs/
    ├── overview-tab.tsx
    ├── eda-tab.tsx
    ├── models-tab.tsx
    ├── forecast-tab.tsx
    ├── risk-tab.tsx
    └── insights-tab.tsx

hooks/
├── use-data-context.ts   # Data context

lib/
└── api-client.ts         # API utilities
```

### Backend Structure
```
backend/
├── main.py              # FastAPI app
├── config.py            # Configuration
├── models/
│   └── schemas.py       # Pydantic models
├── services/
│   ├── file_service.py
│   ├── eda_service.py
│   ├── ml_service.py
│   ├── forecast_service.py
│   ├── risk_service.py
│   └── ai_service.py
└── routes/
    ├── upload.py
    ├── eda.py
    ├── models.py
    ├── forecast.py
    ├── risk.py
    ├── ai_insights.py
    └── reports.py
```

## Making Changes

### Adding a New Feature

1. **Backend**: Create route in appropriate file in `routes/`
2. **Service**: Add business logic to `services/`
3. **Frontend**: Create component in `components/` or `components/tabs/`
4. **API Client**: Update `lib/api-client.ts` if needed

### Adding Dependencies

**Frontend**:
```bash
npm install package-name
```

**Backend**:
```bash
pip install package-name
pip freeze > requirements.txt
```

## Common Tasks

### Run Tests
```bash
# Frontend
npm run lint

# Backend (coming soon)
pytest
```

### Build for Production
```bash
# Frontend
npm run build
npm run start

# Backend
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Database Migrations
```bash
# Create migration (if using Alembic)
alembic revision --autogenerate -m "Description"
alembic upgrade head
```

## Debugging

### Frontend
- Use browser DevTools (F12)
- Check browser console for errors
- Use React DevTools extension

### Backend
- Check console output
- Use `print()` statements for debugging
- Visit http://localhost:8000/docs for API explorer
- Check `.log` files if configured

## Performance Tips

### Frontend
- Use React.memo for expensive components
- Implement virtual scrolling for large lists
- Optimize images with Next.js Image component

### Backend
- Use connection pooling for database
- Cache frequently accessed data
- Use async/await for I/O operations
- Profile with `cProfile` for CPU-bound code
