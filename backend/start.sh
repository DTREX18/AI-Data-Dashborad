#!/bin/bash

# Start FastAPI backend
echo "Starting FastAPI backend..."
cd backend
python -m uvicorn main:app --reload --port 8000 --host 0.0.0.0
