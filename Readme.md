````markdown
# 🚀 HisabDo AI/ML Internship - 5-Day Machine Learning Foundations & Repository Setup

Welcome to the official documentation repository for the **HisabDo Data Analysis & AI/ML Internship**. This project serves as an end-to-end hands-on log capturing the complete machine learning lifecycle—ranging from foundational Python/NumPy array manipulation and Pandas data preprocessing, to Exploratory Data Analysis (EDA), binary classification pipelines, and comparative model evaluation.

---

## 🛠️ Project Architecture & Repository Structure

The repository follows a clean, modular structure organized by daily learning milestones. Each directory operates independently with dedicated scripts, Jupyter Notebooks, datasets, and generated visualizations.

```text
HisabDo-AI-Internship/
│
├── README.md                          # Main internship documentation & technical overview
│
├── day1/                              # Day 1: Python & NumPy Fundamentals
│   ├── main.py                        # Python fundamentals & interactive profiler script
│   └── README.md
│
├── day2/                              # Day 2: Data Manipulation with Pandas
│   ├── day2_main.py                   # Structured data processing, filtering & aggregation
│   └── README.md
│
├── day3/                              # Day 3: Exploratory Data Analysis (EDA) & Data Cleaning
│   ├── day3_student_analysis.ipynb    # End-to-end EDA notebook with feature engineering
│   ├── students_data.csv              # Synthetic student performance dataset
│   ├── chart1_course_averages.png     # Course Performance Comparison Chart
│   ├── chart2_score_distribution.png  # Overall Score Distribution Histogram
│   ├── chart3_attendance_vs_final.png # Attendance vs. Final Exam Correlation Plot
│   └── README.md
│
├── day4/                              # Day 4: Binary Classification Pipeline (Logistic Regression)
│   ├── day4_ml_pipeline.ipynb         # Model training, coefficient analysis & evaluation notebook
│   ├── students_data.csv              # Input student performance dataset
│   ├── chart1_confusion_matrix.png    # Logistic Regression Confusion Matrix
│   ├── chart2_feature_importance.png  # Logistic Regression feature importance weights
│   └── README.md
│
└── day5/                              # Day 5: Model Comparison & Pipeline Evaluation
    ├── day5_model_comparison.ipynb    # Benchmark notebook comparing Logistic Regression vs. Decision Tree
    └── README.md
    │
└── day6/                              # Day 6: Feature Engineering & Hyperparameter Tuning
    ├── day6_hyperparameter_tuning.ipynb# GridSearchCV & model optimization pipeline
    ├── students_data.csv              # Input student performance dataset
    ├── chart_model_comparison.png     # Baseline vs. Tuned metric comparison chart
    ├── chart_roc_curve.png            # ROC-AUC evaluation curves
    └── README.md

```
````

---

## 📅 Day-by-Day Technical Progression

### 🔵 Day 1: Python Fundamentals & Environment Setup

- **Objective:** Establish the development environment and review baseline Python logic and vector manipulation.
- **Theoretical Foundation:** Explored distinctions across Artificial Intelligence (AI), Machine Learning (ML), Deep Learning (DL), and Generative AI (GenAI).
- **Technical Implementation:** Built an interactive CLI application (`main.py`) leveraging dynamic user inputs, custom functions, formatted output strings, and vectorized matrix transformations via **NumPy**.

### 🟢 Day 2: Data Manipulation with Pandas

- **Objective:** Handle structured tabular data loading, missing value handling, and transformation.
- **Data Processing:** Evaluated datasets using **Pandas**, handling dynamic type enforcement and imputation strategies for continuous and categorical variables.
- **Analysis:** Executed query operations to isolate demographic subsets, calculate key statistics (mean, min, max), and restructure columns for downstream tasks.

### 🟣 Day 3: Exploratory Data Analysis (EDA) & Data Visualization

- **Objective:** Extract statistical patterns, clean noisy data, and map continuous/categorical distributions.
- **Data Cleaning & Engineering:** Detected missing values (`NaN`) and imputed them using feature-level mean strategies. Engineered composite metrics such as `Overall_Score` (combining homeworks, midterms, and finals) and identified students at risk (<75% attendance).
- **Visualizations:** Plotted feature distributions via histograms/KDEs and generated correlation heatmaps using **Matplotlib** and **Seaborn**.

### 🔴 Day 4: Binary Classification Pipeline (Logistic Regression)

- **Objective:** Construct an end-to-end supervised machine learning classification pipeline.
- **Target Definition:** Formulated a binary target variable (`Passed`: 1 or 0) derived from student performance thresholds ($\ge 50$).
- **Model Training & Evaluation:** Split features ($X$) and target ($y$) using `train_test_split`, fitted a baseline **Logistic Regression** model, and analyzed model drivers through coefficient weights and Confusion Matrix metrics.

### 🟡 Day 5: Model Comparison Pipeline (Logistic Regression vs. Decision Tree)

- **Objective:** Evaluate linear vs. non-linear classification models under identical data splits.
- **Benchmark Implementation:** Constructed a side-by-side benchmark pipeline comparing **Logistic Regression** against a **Decision Tree Classifier**.
- **Performance Analysis:** Evaluated classification matrices using side-by-side color-coded heatmaps (Blues vs. Greens) and logged comparative metrics (Accuracy, Precision, Recall, F1-Score) to analyze bias-variance trade-offs across distinct decision boundaries.

### Day 6: Feature Engineering & Hyperparameter Tuning (GridSearchCV)

- Objective: Optimize model decision boundaries via advanced feature preprocessing and systematic hyperparameter tuning.
- Feature Engineering & Selection: Handled missing values dynamically, engineered composite performance indices (Dynamic_Score), and applied One-Hot Encoding to categorical variables.
- Feature Scaling: Applied StandardScaler ($Z$-score normalization) exclusively fitted on the training split to eliminate feature magnitude dominance while preventing data leakage.
- Hyperparameter Optimization: Utilized GridSearchCV with 5-fold cross-validation (cv=5) to search over regularization penalties (penalty, C coefficients, solver).
- Evaluation & ROC-AUC: Measured Precision, Recall, F1-Score, and ROC-AUC metrics, visualizing performance gain via comparison bar charts and ROC Curve analysis.

---

## 📊 Summary of EDA & Model Insights

| Metric / Benchmark            | Key Finding / Observation                                                                                                                                                                    |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Top Performing Student**    | Rachel (_AI/ML_) — Overall Score: **96.33**                                                                                                                                                  |
| **Lowest Performing Student** | Peter (_Cyber Security_) — Overall Score: **39.33**                                                                                                                                          |
| **Highest Performing Course** | **Data Science** (Avg: **75.14**) & **AI/ML**                                                                                                                                                |
| **Lowest Performing Course**  | **Cyber Security** (Avg: **61.80**)                                                                                                                                                          |
| **Key Risk Driver**           | Attendance below **75%** strongly correlates with lower final exam scores and failure risk.                                                                                                  |
| **Model Benchmark (Day 5)**   | Evaluated decision boundaries of linear models vs. tree-based non-linear estimators.                                                                                                         |
| **Day 6 Optimization**        | GridSearchCV identified optimal LogisticRegression hyperparameter set: {'C': 1, 'penalty': 'l1', 'solver': 'liblinear'} with 100% Accuracy, F1-Score, and ROC-AUC on test evaluation splits. |

---

## ⚙️ Environment Setup & Execution

1. **Clone the repository:**

```bash
git clone [https://github.com/aysenuryesilova/HisabDo-AI-Internship.git]
cd HisabDo-AI-Internship

```

2. **Install required dependencies:**

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter

```

3. **Launch the development environment:**

```bash
jupyter notebook

```

---

## 💻 Tech Stack & Tools

- **Language:** Python 3.x
- **Data Processing & Analytics:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn (`LogisticRegression`, `DecisionTreeClassifier`,`GridSearchCV`, `StandardScaler`, `train_test_split`, `metrics`)
- **Data Visualization:** Matplotlib, Seaborn
- **Environment & Version Control:** VS Code, Jupyter Notebook, Windows Terminal, Git, GitHub

---

## 👤 Author & Contact

**Ayşe Nur Yeşilova**

_AI/ML Intern at HisabDo_

- **GitHub:** [@Aysenuryesilova]

```

```
