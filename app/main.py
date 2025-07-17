from fastapi import FastAPI
from app.schemas import LoanApplication
from app.model import predict_loan_default

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Loan Default Predictor is running."}

@app.post("/predict")
def predict(data: LoanApplication):
    result = predict_loan_default(data.Pclass, data.Sex, data.Age)
    return {"default_risk": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)