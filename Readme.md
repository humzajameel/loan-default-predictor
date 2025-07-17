# Loan Default Predictor 🚀

A FastAPI-based machine learning API that predicts whether a person is likely to default on a loan. Trained with scikit-learn and deployed via Docker + Railway.

---

## 🧠 Model

- Logistic Regression
- Trained using joblib
- Features: Person Class, age, sex, etc.

---

## 📦 Tech Stack

- Python
- FastAPI
- scikit-learn
- Docker
- Railway (deployment)

---

## 🚀 Live Demo

👉 [https://loan-default-predictor-production.up.railway.app/docs](https://loan-default-predictor-production.up.railway.app/docs)

Use `/predict` endpoint with POST method and JSON input.

Example request:

```json
{
  "Pclass": 2,
  "Sex": 1,
  "Age": 40
}

Output:
{
    "default_risk": true
}
```
