import joblib
import numpy as np

# Load the model when the module is imported
model = joblib.load("model.joblib")

def predict_loan_default(Pclass: int, Sex: int, Age: float) -> bool:
    X = np.array([[Pclass, Sex, Age]])
    prediction = model.predict(X)
    return bool(prediction[0])
