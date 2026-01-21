# High School Graduation Prediction Project

## Executive Summary

This project explores how machine learning can support **early identification of students at risk of not graduating on time or maintaining regular attendance**, using historical academic and engagement data.

I built and evaluated a **Random Forest–based early warning model** using real district data under FERPA constraints, with a strong emphasis on **interpretability, ethical use, and decision support rather than automation**.

Because the original dataset contains protected student information, this public repository focuses on **methodology, modeling decisions, explainability, and stakeholder communication**, and uses **synthetic data** for demonstration purposes.

---

## 🔗 Project Context & Storytelling

- 📝 **Blog post:**  
  From Student Learning to Machine Learning: Predicting High School Graduation with Data  
  https://randomforestforthetrees.medium.com/from-student-learning-to-machine-learning-predicting-high-school-graduation-with-data-318497426015

- 📑 **Stakeholder presentation:**  
  Project slide deck (PDF)  
  https://github.com/mtchynkstff/high-school-graduation/blob/main/reports/Plymouth-HS_Data-Analysis_013025.pdf

These artifacts were created for non-technical stakeholders and reflect how insights would be communicated in a real school district setting.

---

## 📁 Repository Structure

data/                    # synthetic or local student-level dataset (not tracked)  
notebooks/               # main analysis notebook  
reports/  
  figures/               # exported charts for README & slides  
  Plymouth_Graduation_Project_Presentation.pdf  
src/                     # helper scripts (e.g., synthetic data generator)  
requirements.txt         # dependencies  
README.md                # project documentation  

---

## 🚀 How to Run (Synthetic Data Only)

Install dependencies:

pip install -r requirements.txt

Generate synthetic data:

python src/generate_synthetic.py

This will create:

data/synthetic_graduation_data.csv

Launch Jupyter:

jupyter notebook notebooks/Plymouth-Graduation-Project-Final-Clean_020325.ipynb

When running outside a secure district environment, update the notebook to point at:

data/synthetic_graduation_data.csv

Note: Synthetic data is provided to illustrate pipeline structure and feature engineering only. Results are not intended to replicate the original analysis.

---

## ▶️ Open in Google Colab

https://colab.research.google.com/github/mtchynkstff/high-school-graduation/blob/main/notebooks/Plymouth-Graduation-Project-Final-Clean_020325.ipynb

---

## 📊 Problem & Data

### Goal

Predict whether a student will:

- Graduate on time  
- Maintain regular attendance  

using historical academic, behavioral, and assessment data.

The intent is to support **earlier, targeted interventions**, not to label or automate decisions about students.

### Conceptual Features

- GPA and course grades  
- Attendance rate and absences  
- Credits earned toward graduation  
- Assessment scores (e.g., ELA, Math)  

### Targets

- on_time_graduation (binary)  
- regular_attendance (binary)  

---

## 🧠 Methods

The main analysis notebook follows these stages:

1. Data import and cleaning  
2. Exploratory data analysis (EDA)  
3. Feature engineering  
4. Modeling with Random Forest  
5. Evaluation (ROC-AUC, precision/recall, confusion matrices)  
6. Explainability using feature importance and SHAP  
7. Insights, limitations, and recommendations  

---

## 🧩 Model Selection Rationale

Random Forest was selected because it:

- Captures non-linear relationships common in student academic and behavioral data  
- Handles mixed feature types with minimal preprocessing  
- Balances predictive performance with interpretability  

For a district-facing early warning system, this tradeoff was preferred over simpler linear models or more complex black-box approaches.

If data access were available today, I would benchmark against logistic regression (for calibration and transparency) and gradient boosting models (for performance tradeoffs).

---

## 🔒 Data Access & Privacy

- The original analysis was conducted using **real student-level data** under district authorization and FERPA compliance.  
- I no longer have access to the raw dataset, and the notebook results are preserved as originally analyzed.  
- This public repository contains **no real student data**.  
- Synthetic data is included solely to demonstrate pipeline structure and modeling workflow.

This project intentionally prioritizes **ethical handling of educational data** over full reproducibility.

---

## 📌 Future Extensions (If Data Access Were Available)

- Hyperparameter tuning and probability calibration  
- Subgroup fairness and bias analysis  
- Time-based validation to simulate early-warning deployment  
- Demonstration interface using synthetic data only  

_Last updated: 2026-01-20_
