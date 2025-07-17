from pydantic import BaseModel

class LoanApplication(BaseModel):
    Pclass: int
    Sex: int  # 0 = male, 1 = female
    Age: float
