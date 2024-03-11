from fastapi import APIRouter, Depends, status, HTTPException, Response
from ..database import get_db
from .. import schemas, models, utils
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix='/loans',
    tags=['Loans']
)

@router.get("/", response_model=List[schemas.LoanResponse])
async def get_loans(db: Session = Depends(get_db), limit: int = 10):
    loans = db.query(models.Loans).limit(limit).all()

    return loans


@router.post("/", response_model=schemas.NewLoanResponse)
async def create_loan(loan: schemas.LoanInput, db: Session = Depends(get_db)):
    new_loan = models.Loans(**loan.model_dump())
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)

    # calculate the necessary figures
    principal_loan_amount = new_loan.desired_loan_amount
    interest_rate = utils.calculate_interest_rate()
    number_of_payments = utils.calculate_number_of_payments(new_loan.loan_term)
    monthly_payment_amount = utils.calculate_payment_amount(principal_loan_amount, interest_rate, number_of_payments)
    total_interest_amount = utils.calculate_total_interest(principal_loan_amount, interest_rate, new_loan.loan_term)
    
    response = {
        'principal_loan_amount': principal_loan_amount,
        'monthly_payment_amount': monthly_payment_amount,
        'total_interest_amount': total_interest_amount,
        'loan_term': new_loan.loan_term
    }

    return response
