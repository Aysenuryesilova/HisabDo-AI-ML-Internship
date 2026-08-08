---
# HisabDo AI/ML Integration Report – Day 8: Capstone Project (Phase 1 & 2)

## 📌 Introduction

This document outlines 5 practical Artificial Intelligence and Machine Learning use cases tailored for the **HisabDo** financial tracking platform (Website, Web Application, and Mobile Application).
---

## 💡 Part 1: Top 5 AI/ML Use Cases for HisabDo

### 1. Smart Expense Categorization (Akıllı Harcama Kategorizasyonu)

- **Problem Statement:** Users often forget or find it tedious to manually categorize every daily transaction (e.g., groceries, fuel, dining), leading to messy financial records.
- **Proposed AI Solution:** Use a text classification machine learning model (NLP) to automatically categorize transaction descriptions/merchant names into appropriate budget categories.
- **Input Data Required:** Transaction description text (e.g., "Starbucks Coffee", "Shell Petrol Station") and user history.
- **Expected Output:** Predicted category label (e.g., "Food & Dining", "Transportation") with a confidence score.
- **AI/ML Technology:** Natural Language Processing (NLP), Scikit-Learn (TF-IDF + Logistic Regression/Random Forest).
- **Possible API/Model:** Custom Scikit-Learn pipeline or transformer-based text classifier.
- **Integration Point:** Mobile Application & Web Application (triggered upon adding a transaction).

### 2. Receipt OCR & Automated Expense Scanner (Fiş OCR Tarayıcı)

- **Problem Statement:** Manual data entry of paper receipts is time-consuming and prone to human typos.
- **Proposed AI Solution:** Implement Optical Character Recognition (OCR) combined with an LLM/Regex extractor to automatically pull total amounts, dates, and merchant names from receipt photos.
- **Input Data Required:** Image file of a physical receipt (.jpg, .png).
- **Expected Output:** Structured JSON containing extracted fields: `Merchant`, `Date`, `Total Amount`, and `Items`.
- **AI/ML Technology:** Computer Vision, OCR (Optical Character Recognition).
- **Possible API/Model:** Tesseract OCR, Google Cloud Vision API, or OpenAI Vision API.
- **Integration Point:** Mobile Application (Camera scan feature).

### 3. AI Financial Assistant & Chatbot (AI Finansal Asistan & Sohbet Botu)

- **Problem Statement:** Users struggle to analyze their spending trends and require conversational guidance on how to save money.
- **Proposed AI Solution:** A conversational AI assistant trained on the user's financial data to answer questions like _"How much did I spend on dining out last week?"_ or _"Can I afford a vacation this month?"_
- **Input Data Required:** User's transaction history, current budget limits, and user text prompts.
- **Expected Output:** Natural language text response answering financial queries and offering advice.
- **AI/ML Technology:** Large Language Models (LLMs), Retrieval-Augmented Generation (RAG).
- **Possible API/Model:** OpenAI GPT-4o mini, Anthropic Claude, or open-source Llama 3 via LangChain.
- **Integration Point:** Mobile Application & Web Application (Dedicated chat screen).

### 4. Predictive Budget Recommendations & Alerts (Tahminsel Bütçe Önerileri)

- **Problem Statement:** Users often exceed their monthly budget limits before realizing it, due to lack of early warnings.
- **Proposed AI Solution:** Time-series forecasting and anomaly detection algorithms to predict end-of-month spending and alert users if they are on track to overspend.
- **Input Data Required:** Historical daily spending aggregates, current income, and active budget goals.
- **Expected Output:** Predictive alerts (e.g., _"At your current spending rate, you will exceed your grocery budget in 5 days"_).
- **AI/ML Technology:** Time-Series Analysis, Regression Models, Anomaly Detection.
- **Possible API/Model:** ARIMA, Facebook Prophet, or Scikit-Learn regression models.
- **Integration Point:** Mobile Application (Smart Notifications) & Web Dashboard.

### 5. Smart Reminder Intelligence (Akıllı Hatırlatıcı Zekası)

- **Problem Statement:** Missing bill payment deadlines results in late fees and financial stress.
- **Proposed AI Solution:** Predict recurring payment patterns and send proactive smart reminders before bills are due, factoring in the user's usual cash flow timing.
- **Input Data Required:** Recurring transaction timestamps and historical payment delays.
- **Expected Output:** Automated reminder notification with suggested payment dates.
- **AI/ML Technology:** Pattern Recognition & Classification.
- **Possible API/Model:** Custom rule-based clustering and decision tree algorithms.
- **Integration Point:** Mobile Application (Push notifications).

---

## 🏗️ Part 2: Top 2 Features Technical Architecture

From the list above, the **Smart Expense Categorization** and **AI Financial Assistant** features have been selected for core architectural design.

### Feature 1: Smart Expense Categorization Architecture

This architecture details how a transaction text is processed and classified instantly.

```text
[ User ]
   │
   ▼ (Enters text: "Uber Ride")
[ Mobile / Web Application ]
   │
   ▼ (Sends POST request with description)
[ FastAPI Backend Service ]
   │
   ▼ (Preprocesses text & applies TF-IDF)
[ ML Model / API (Scikit-Learn Classifier) ]
   │
   ▼ (Returns predicted category: "Transportation", Confidence: 0.95)
[ JSON Response ] ➔ Displayed back to User UI

```

### Feature 2: AI Financial Assistant Architecture

This architecture outlines how conversational queries interact securely with user financial data via RAG (Retrieval-Augmented Generation).

```text
[ User ]
   │
   ▼ (Asks: "How much did I spend on food?")
[ Mobile / Web Application ]
   │
   ▼ (API Request)
[ FastAPI Backend Service ] ──(Fetches user SQL data)──> [ Database ]
   │
   ▼ (Combines prompt + user data context)
[ LLM Provider API (OpenAI / Claude) ]
   │
   ▼ (Generates natural language answer)
[ JSON Response ] ➔ Displayed in Chat UI to User

```
