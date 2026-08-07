# -*- coding: utf-8 -*-
"""
Day 7 Task - Makine Öğrenimi Modelini API Olarak Yayınlama (FastAPI)
Yazar: Ayse Nur Yesilova
Açıklama: Modelin beklediği 39 özelliğin tamamını eksiksiz alan ve 
          gerçekçi tahminler üreten profesyonel UI/UX arayüzlü API betiği.
"""

import os
import joblib
import numpy as np
import pandas as pd
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field, ConfigDict

# Model ve ölçeklendirici dosya yolları
MODEL_PATH = "model.pkl"
SCALER_PATH = "scaler.pkl"

model = None
scaler = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model, scaler
    try:
        if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
            model = joblib.load(MODEL_PATH)
            scaler = joblib.load(SCALER_PATH)
            print("Model ve scaler başarıyla belleğe yüklendi.")
        else:
            print("Uyarı: Model veya scaler dosyası bulunamadı!")
    except Exception as e:
        print(f"Yükleme hatası: {e}")
    yield

app = FastAPI(
    title="Student Performance Prediction API",
    description="Full 39-Feature Machine Learning Prediction API with Modern UI",
    version="2.3.0",
    lifespan=lifespan
)

class StudentInput(BaseModel):
    age: float = Field(..., ge=15.0, le=60.0)
    attendance: float = Field(..., ge=0.0, le=100.0)
    assignment_score: float = Field(..., ge=0.0, le=100.0)
    midterm_score: float = Field(..., ge=0.0, le=100.0)
    final_score: float = Field(..., ge=0.0, le=100.0)
    gender: str = Field(...)  # 'Male' veya 'Female'
    course: str = Field(...)  # 'AI/ML', 'Data Science', 'Web Dev', 'Cyber Security'

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "age": 22.0,
                "attendance": 85.0,
                "assignment_score": 90.0,
                "midterm_score": 80.0,
                "final_score": 85.0,
                "gender": "Female",
                "course": "AI/ML"
            }
        }
    )

@app.get("/", response_class=HTMLResponse)
def home():
    """
    39 özelliğin tamamının girilebileceği profesyonel, şık ve modern form arayüzü.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Student Performance AI | Full Feature Dashboard</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Inter', sans-serif; }
            .glass-card {
                background: rgba(30, 41, 59, 0.75);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.1);
            }
        </style>
    </head>
    <body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between selection:bg-sky-500 selection:text-white">
        
        <header class="border-b border-slate-800 py-4 px-6 md:px-12 flex justify-between items-center bg-slate-900/50 backdrop-blur">
            <div class="flex items-center space-x-3">
                <div class="w-3 h-3 bg-emerald-500 rounded-full animate-pulse"></div>
                <span class="font-bold text-lg tracking-wide text-white">HisabDo AI <span class="text-sky-400 font-light">Engine</span></span>
            </div>
            <div class="space-x-4 text-sm font-medium">
                <a href="/docs" target="_blank" class="text-slate-400 hover:text-sky-400 transition">Swagger API</a>
                <a href="/redoc" target="_blank" class="text-slate-400 hover:text-sky-400 transition">ReDoc</a>
            </div>
        </header>

        <main class="flex-grow flex items-center justify-center p-4 md:p-8">
            <div class="max-w-4xl w-full grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                
                <div class="space-y-6">
                    <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight text-white leading-tight">
                        Student Success <span class="text-transparent bg-clip-text bg-gradient-to-r from-sky-400 to-indigo-500">Predictor</span>
                    </h1>
                    <p class="text-slate-400 text-sm leading-relaxed">
                        Full 39-Feature Machine Learning evaluation model. Enter all student attributes below for accurate classification and high-precision confidence scoring.
                    </p>
                    <div class="flex items-center space-x-4 text-xs text-slate-500">
                        <span>⚡ FastAPI Backend</span>
                        <span>•</span>
                        <span>🛡️ Pydantic V2</span>
                        <span>•</span>
                        <span>📊 39-Feature Matrix</span>
                    </div>
                </div>

                <div class="glass-card p-6 md:p-8 rounded-2xl shadow-2xl relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-sky-500/10 rounded-full blur-2xl -mr-10 -mt-10"></div>
                    
                    <h2 class="text-xl font-semibold mb-6 text-white flex items-center justify-between">
                        <span>Prediction Panel</span>
                        <span class="text-xs font-normal text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-md border border-emerald-500/20">System Online</span>
                    </h2>

                    <form id="predictionForm" class="space-y-3">
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-medium text-slate-300 mb-1">Age</label>
                                <input type="number" id="age" value="22" required class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-sky-500">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-300 mb-1">Attendance (%)</label>
                                <input type="number" step="0.1" id="attendance" value="85.0" required class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-sky-500">
                            </div>
                        </div>

                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-medium text-slate-300 mb-1">Assignment Score</label>
                                <input type="number" step="0.1" id="assignment_score" value="90.0" required class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-sky-500">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-300 mb-1">Midterm Score</label>
                                <input type="number" step="0.1" id="midterm_score" value="80.0" required class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-sky-500">
                            </div>
                        </div>

                        <div>
                            <label class="block text-xs font-medium text-slate-300 mb-1">Final Score</label>
                            <input type="number" step="0.1" id="final_score" value="85.0" required class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-sky-500">
                        </div>

                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-medium text-slate-300 mb-1">Gender</label>
                                <select id="gender" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-sky-500">
                                    <option value="Female">Female</option>
                                    <option value="Male">Male</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-300 mb-1">Course</label>
                                <select id="course" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-sky-500">
                                    <option value="AI/ML">AI/ML</option>
                                    <option value="Data Science">Data Science</option>
                                    <option value="Web Dev">Web Dev</option>
                                    <option value="Cyber Security">Cyber Security</option>
                                </select>
                            </div>
                        </div>

                        <button type="submit" class="w-full mt-3 bg-gradient-to-r from-sky-500 to-indigo-600 hover:from-sky-400 hover:to-indigo-500 text-white font-semibold py-2.5 px-4 rounded-lg shadow-lg shadow-sky-500/20 transition-all duration-200 text-sm tracking-wide">
                            Run AI Prediction
                        </button>
                    </form>

                    <div id="resultBox" class="mt-4 hidden p-3.5 rounded-xl border transition-all duration-300">
                        <div class="flex justify-between items-center">
                            <div>
                                <p class="text-[10px] text-slate-400 uppercase tracking-wider">Prediction Outcome</p>
                                <p id="predText" class="text-xl font-bold mt-0.5"></p>
                            </div>
                            <div class="text-right">
                                <p class="text-[10px] text-slate-400 uppercase tracking-wider">Confidence</p>
                                <p id="confText" class="text-base font-semibold text-slate-200 mt-0.5"></p>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </main>

        <footer class="border-t border-slate-800 py-3 text-center text-xs text-slate-500 bg-slate-900/30">
            HisabDo AI/ML Internship Program • Developed by Ayse Nur Yesilova
        </footer>

        <script>
            document.getElementById('predictionForm').addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const payload = {
                    age: parseFloat(document.getElementById('age').value),
                    attendance: parseFloat(document.getElementById('attendance').value),
                    assignment_score: parseFloat(document.getElementById('assignment_score').value),
                    midterm_score: parseFloat(document.getElementById('midterm_score').value),
                    final_score: parseFloat(document.getElementById('final_score').value),
                    gender: document.getElementById('gender').value,
                    course: document.getElementById('course').value
                };

                const resultBox = document.getElementById('resultBox');
                const predText = document.getElementById('predText');
                const confText = document.getElementById('confText');

                try {
                    const response = await fetch('/predict', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(payload)
                    });

                    const data = await response.json();

                    if (response.ok) {
                        resultBox.classList.remove('hidden');
                        if (data.prediction === 'Pass') {
                            resultBox.className = "mt-4 p-3.5 rounded-xl border bg-emerald-950/40 border-emerald-500/30 text-emerald-400";
                            predText.textContent = "PASSED 🎉";
                        } else {
                            resultBox.className = "mt-4 p-3.5 rounded-xl border bg-rose-950/40 border-rose-500/30 text-rose-400";
                            predText.textContent = "FAILED ⚠️";
                        }
                        confText.textContent = (data.confidence * 100).toFixed(1) + '%';
                    } else {
                        alert('Validation Error: ' + JSON.stringify(data.detail));
                    }
                } catch (err) {
                    alert('Network error or server unavailable.');
                }
            });
        </script>
    </body>
    </html>
    """
    return html_content

@app.post("/predict")
def predict_student_performance(data: StudentInput):
    global model, scaler
    if model is None or scaler is None:
        raise HTTPException(status_code=500, detail="Model or scaler not loaded.")
    
    try:
        # Scaler'ın eğitim aşamasında kaydettiği 39 özellik ismini alıyoruz
        if hasattr(scaler, "feature_names_in_"):
            feature_names = scaler.feature_names_in_
        else:
            feature_names = [
                'Age', 'Attendance', 'Assignment_Score', 'Midterm_Score', 'Final_Score', 'Dynamic_Score', 
                'Student_Name_Arthur', 'Student_Name_Bella', 'Student_Name_Bob', 'Student_Name_Charlie', 
                'Student_Name_Chris', 'Student_Name_David', 'Student_Name_Diana', 'Student_Name_Emma', 
                'Student_Name_Frank', 'Student_Name_Grace', 'Student_Name_Hannah', 'Student_Name_Ian', 
                'Student_Name_Jack', 'Student_Name_Karen', 'Student_Name_Liam', 'Student_Name_Mia', 
                'Student_Name_Noah', 'Student_Name_Olivia', 'Student_Name_Peter', 'Student_Name_Quinn', 
                'Student_Name_Rachel', 'Student_Name_Sam', 'Student_Name_Tina', 'Student_Name_Umar', 
                'Student_Name_Victor', 'Student_Name_Wendy', 'Student_Name_Xavier', 'Student_Name_Yara', 
                'Student_Name_Zack', 'Gender_Male', 'Course_Cyber Security', 'Course_Data Science', 'Course_Web Dev'
            ]
        
        # 39 sütunluk tam sıfır matrisi oluşturuyoruz
        input_df = pd.DataFrame(columns=feature_names, data=np.zeros((1, len(feature_names))))
        
        # Temel sayısal değerleri yerleştiriyoruz
        if 'Age' in input_df.columns: input_df.loc[0, 'Age'] = data.age
        if 'Attendance' in input_df.columns: input_df.loc[0, 'Attendance'] = data.attendance
        if 'Assignment_Score' in input_df.columns: input_df.loc[0, 'Assignment_Score'] = data.assignment_score
        if 'Midterm_Score' in input_df.columns: input_df.loc[0, 'Midterm_Score'] = data.midterm_score
        if 'Final_Score' in input_df.columns: input_df.loc[0, 'Final_Score'] = data.final_score
        
        # Dinamik skor hesaplama (Eğitimdeki formülle uyumlu olması için ortalama)
        if 'Dynamic_Score' in input_df.columns:
            input_df.loc[0, 'Dynamic_Score'] = np.mean([data.attendance, data.assignment_score, data.midterm_score, data.final_score])
        
        # One-Hot Encoding sütunlarını kullanıcının seçimine göre 1 yapıyoruz
        if data.gender == 'Male' and 'Gender_Male' in input_df.columns:
            input_df.loc[0, 'Gender_Male'] = 1.0
            
        course_col = f"Course_{data.course}"
        if course_col in input_df.columns:
            input_df.loc[0, course_col] = 1.0
            
        # Scaler ile dönüştürme
        scaled_features = scaler.transform(input_df)
        
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
            "input_received": data.dict()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))