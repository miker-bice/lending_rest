from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime

class LoanInput(BaseModel):
    fist_name: str = Field(min_length=1, max_length=30)
    last_name: str = Field(min_length=1, max_length=30)
    desired_loan_amount: float = Field(ge=1000, le=10000)
    loan_term: Literal[3, 6, 9, 12, 15, 18]

class LoanResponse(LoanInput):
    id: int
    created_at: datetime

    class Config():
        from_attributes = True


class NewLoanResponse(BaseModel):
    principal_loan_amount: float
    monthly_payment_amount: float
    total_interest_amount: float
    loan_term: int
    total_sum_payments: float
    
