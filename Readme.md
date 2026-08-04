# 🚀 HisabDo AI/ML Internship - Daily Hands-On Projects

Welcome to my repository for the **HisabDo AI/ML Internship Bootcamp**. This repository acts as a comprehensive documentation of my daily progress, technical implementations, data analyses, and machine learning fundamentals.

---

## 📂 Repository Structure

```text
.
├── day1/
│   └── main.py                     # Python fundamentals & interactive student profiler
├── day2/
│   └── day2_main.py                # Pandas operations, data filtering, and basic stats
├── day3/
│   ├── day3_student_analysis.ipynb # End-to-end Data Cleaning, EDA & Matplotlib charts
│   ├── students_data.csv           # 30-record synthetic student dataset
│   ├── chart1_course_averages.png  # Course Performance Comparison Chart
│   ├── chart2_score_distribution.png # Overall Score Distribution Histogram
│   └── chart3_attendance_vs_final.png# Attendance vs Final Exam Correlation Plot
├── day4/
│   ├── day4_ml_pipeline.ipynb      # Complete ML training & evaluation notebook
│   ├── students_data.csv           # Input student performance dataset
│   ├── chart1_confusion_matrix.png # Confusion Matrix heat map visualization
│   └── chart2_feature_importance.png# Logistic Regression coefficient weights
└── README.md                       # Main internship documentation

```

---

## 🛠️ Daily Highlights & Key Achievements

### 🔵 Day 1: Python Fundamentals & Core Concepts

- **Theoretical Foundation:** Explored core distinctions between Artificial Intelligence (AI), Machine Learning (ML), Deep Learning (DL), and Generative AI (GenAI).
- **Technical Implementation:** Built an interactive command-line Python application (`main.py`) utilizing dynamic user inputs, custom calculation functions, and formatted string outputs.

### 🟢 Day 2: Structured Data Handling with Pandas

- **Data Processing:** Worked with tabular datasets using the Python Pandas library.
- **Analysis:** Executed queries to filter student performance, calculated statistical summaries (mean, min, max), and identified target metrics across multiple demographic groups.

### 🟣 Day 3: Jupyter Analysis, Data Cleaning & Visualizations (EDA)

- **Environment:** Transitioned to Jupyter Notebook (`.ipynb`) for dynamic code execution and reproducible exploratory data analysis (EDA).
- **Data Cleaning & Imputation:** Detected missing records (`NaN`) in performance columns and imputed them using feature-level mean strategies to preserve data integrity.
- **Metrics Engineering:** Created calculated fields such as `Overall_Score` to evaluate holistic performance combining homework, midterms, and finals.
- **Risk Analysis:** Identified students with < 75% attendance (At-Risk category).

### 🔴 Day 4: Student Performance Prediction with Machine Learning

- **Target Definition:** Created a binary target (`Passed`: 1 or 0) based on overall score thresholds ($\ge 50$).
- **Model Training:** Built an end-to-end classification pipeline using **Logistic Regression** via `scikit-learn`.
- **Evaluation & Insights:** Evaluated outcomes with Confusion Matrix and analyzed feature coefficients to understand performance drivers.

---

## 📊 Summary of Insights (Day 3 EDA)

| Metric                        | Key Finding                                                            |
| ----------------------------- | ---------------------------------------------------------------------- |
| **Top Performing Student**    | Rachel (_AI/ML_) — Overall Score: **96.33**                            |
| **Lowest Performing Student** | Peter (_Cyber Security_) — Overall Score: **39.33**                    |
| **Highest Performing Course** | **Data Science** (Avg: **75.14**) & **AI/ML**                          |
| **Lowest Performing Course**  | **Cyber Security** (Avg: **61.80**)                                    |
| **Key Risk Factor**           | Attendance below 75% directly correlates with lower final exam scores. |

---

## 💻 Tech Stack & Tools

- **Language:** Python 3.x
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn (Logistic Regression)
- **Visualization:** Matplotlib, Seaborn
- **Environment:** VS Code, Jupyter Notebook, Git, GitHub

---

## 👤 Author & Contact

**Ayşe Nur Yeşilova**

_AI/ML Intern at HisabDo_

- GitHub: [@Aysenuryesilova](https://github.com/Aysenuryesilova)
