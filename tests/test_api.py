from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_endpoint():
    payload = {
        "Pclass": 2,
        "Sex": 1,
        "Age": 30
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "default_risk" in response.json()
    assert isinstance(response.json()["default_risk"], bool)
