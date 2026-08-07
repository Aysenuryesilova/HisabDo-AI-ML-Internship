# -*- coding: utf-8 -*-
"""
Day 7 Task - Machine Learning Model Deployment as an API (FastAPI)
Author: Ayse Nur Yesilova
Description: This script loads the trained student performance model and scaler,
             validates incoming requests using Pydantic, and serves predictions via a REST API.
"""

import os
import joblib
import numpy as np
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field, ConfigDict

# Define file paths for the saved machine learning model and scaler
MODEL_PATH = "model.pkl"
SCALER_PATH = "scaler.pkl"

# Global variables to store loaded model and scaler
model = None
scaler = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Modern FastAPI Lifespan context manager to load artifacts on startup.
    """
    global model, scaler
    try:
        if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
            model = joblib.load(MODEL_PATH)
            scaler = joblib.load(SCALER_PATH)
            print("Model and scaler successfully loaded into memory.")
        else:
            print("Warning: Model or scaler file not found! Please train and save them first.")
    except Exception as e:
        print(f"Error loading artifacts: {e}")
    yield

# Initialize FastAPI application with professional English metadata
app = FastAPI(
    title="Student Performance Prediction API",
    description="An advanced production-ready AI web service to predict student academic success.",
    version="1.0.0",
    lifespan=lifespan
)

class StudentInput(BaseModel):
    """
    Pydantic Model for strict input validation with range constraints (0-100).
    """
    attendance: float = Field(..., ge=0.0, le=100.0, description="Student attendance percentage")
    assignment_score: float = Field(..., ge=0.0, le=100.0, description="Assignment score")
    midterm_score: float = Field(..., ge=0.0, le=100.0, description="Midterm exam score")
    final_score: float = Field(..., ge=0.0, le=100.0, description="Final exam score")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "attendance": 85.0,
                "assignment_score": 90.0,
                "midterm_score": 80.0,
                "final_score": 85.0
            }
        }
    )

@app.get("/", response_class=HTMLResponse)
def home():
    """
    Custom, modern, dark-themed landing page instead of raw JSON or boring docs.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Student Performance AI API</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #0f172a;
                color: #f8fafc;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background: #1e293b;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.3);
                text-align: center;
                max-width: 500px;
                width: 100%;
                border: 1px solid #334155;
            }
            h1 { color: #38bdf8; margin-bottom: 10px; font-size: 24px; }
            p { color: #94a3b8; font-size: 15px; margin-bottom: 25px; }
            .btn-group { display: flex; gap: 15px; justify-content: center; }
            a {
                text-decoration: none;
                padding: 12px 20px;
                border-radius: 8px;
                font-weight: bold;
                font-size: 14px;
                transition: all 0.3s ease;
            }
            .btn-docs { background: #38bdf8; color: #0f172a; }
            .btn-docs:hover { background: #0ea5e9; }
            .btn-redoc { background: #334155; color: #f8fafc; border: 1px solid #475569; }
            .btn-redoc:hover { background: #475569; }
            .status { margin-top: 20px; font-size: 12px; color: #4ade80; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Student Performance AI API</h1>
            <p>HisabDo AI/ML Internship - Day 7 Production API Service is up and running successfully.</p>
            <div class="btn-group">
                <a href="/docs" class="btn-docs">Swagger UI Docs</a>
                <a href="/redoc" class="btn-redoc">ReDoc Docs</a>
            </div>
            <div class="status">● System Online & Model Loaded</div>
        </div>
    </body>
    </html>
    """
    return html_content

@app.post("/predict")
def predict_student_performance(data: StudentInput):
    """
    POST Endpoint: Accepts student features, scales them, and returns pass/fail prediction with confidence.
    """
    global model, scaler
    
    if model is None or scaler is None:
        raise HTTPException(
            status_code=500, 
            detail="Model or scaler not loaded on the server. Please check server logs."
        )
    
    try:
        input_features = np.array([[
            data.attendance,
            data.assignment_score,
            data.midterm_score,
            data.final_score
        ]])
        
        scaled_features = scaler.transform(input_features)
        prediction_numeric = model.predict(scaled_features)[0]
        
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(scaled_features)[0]
            confidence_score = float(np.max(probabilities))
        else:
            confidence_score = 1.0
            
        prediction_label = "Pass" if prediction_numeric == 1 else "Fail"
        
        return {
            "prediction": prediction_label,
            "prediction_code": int(prediction_numeric),
            "confidence": round(confidence_score, 4),
            "input_received": {
                "attendance": data.attendance,
                "assignment_score": data.assignment_score,
                "midterm_score": data.midterm_score,
                "final_score": data.final_score
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")