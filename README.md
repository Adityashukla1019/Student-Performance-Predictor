# Smart Student Performance Predictor

End‑to‑end Data Science project predicting Math score from Reading & Writing scores using classic **Students Performance** dataset (Kaggle). Includes EDA, model training, and a simple Streamlit app.

## Project Structure
```
student-performance-predictor/
├── app.py                   # Streamlit app to make predictions
├── requirements.txt
├── .gitignore
├── README.md
├── LICENSE
├── notebooks/
│   └── EDA_and_Model.ipynb  # Starter notebook
├── src/
│   ├── data_preprocessing.py
│   ├── train_model.py
│   └── predict.py
├── data/                    # Put StudentsPerformance.csv here (not tracked by git)
└── models/
    └── model.pkl            # Created after training
```

## Dataset
- Download **StudentsPerformance.csv** from Kaggle: "Students Performance in Exams" by spscientist.
- Place the file at `data/StudentsPerformance.csv`.

## Quickstart
```bash
# 1) Create & activate a virtual environment (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2) Install dependencies
pip install -r requirements.txt

# 3) Train model (reads data/StudentsPerformance.csv, writes models/model.pkl)
python src/train_model.py

# 4) Run the Streamlit app
streamlit run app.py
```

Open the URL Streamlit prints (usually http://localhost:8501) to try predictions.

## What it predicts
This starter uses **Reading** and **Writing** scores to predict the **Math** score via regression (Linear Regression or Random Forest; the script picks the better one by RMSE). This is purely for demo — you can extend it with richer features/datasets (UCI "Student Performance", attendance, study-time, etc.).

## Next steps
- Add more features and compare models (XGBoost, CatBoost).
- Improve EDA visuals and insights.
- Package the model with `skops` or `joblib` and add versioning.
- Deploy publicly (Streamlit Community Cloud).

## Badges (add later)
- Tests: pytest + CI
- Code style: black + flake8
- License: MIT

