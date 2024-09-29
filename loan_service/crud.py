from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import models, schemas
from utils import validate_amount,generate_unique_no,validate_duration_months

def create_loan(db: Session, loan: schemas.LoanCreate):
     
    if not validate_duration_months(loan.duration_months):
        raise HTTPException(status_code=400, detail="Loan duration should be greater than or equal to 24")

    if not validate_amount(loan.amount):
        raise HTTPException(status_code=400, detail="Loan amount should be greater than 10000 and lesser than 10000000")
    
    customer_loan_present = db.query(models.Loan).filter(models.Loan.customer_id == loan.customer_id, models.Loan.loan_type == loan.loan_type).first()
    customer_id_present=db.query(models.Loan).filter(models.Loan.customer_id == loan.customer_id).first()
    loan_type_present= db.query(models.Loan).filter(models.Loan.loan_type == loan.loan_type).first()


    if not customer_loan_present:
        loan_no=generate_unique_no(loan.loan_type)
        db_loan = models.Loan(
            loan_no=loan_no,
            loan_type=loan.loan_type,
            amount = loan.amount,
            interest_rate = loan.interest_rate,
            duration_months = loan.duration_months,
            customer_id = loan.customer_id
            )
        db.add(db_loan)
        db.commit()
        db.refresh(db_loan)
        return db_loan
    elif customer_id_present:
       if not loan_type_present:
        loan_no=generate_unique_no(loan.loan_type)
        db_loan = models.Loan(
            loan_no=loan_no,
            loan_type=loan.loan_type,
            amount = loan.amount,
            interest_rate = loan.interest_rate,
            duration_months = loan.duration_months,
            customer_id = loan.customer_id
            )
        db.add(db_loan)
        db.commit()
        db.refresh(db_loan)
        return db_loan 
       else:
        raise HTTPException(status_code=404, detail="Already applied for loan")
    else:
        raise HTTPException(status_code=404, detail="Already applied for loan")


def get_loan_by_customer_Id(db: Session, customer_id: int):
    loan = db.query(models.Loan).filter(models.Loan.customer_id == customer_id).all()

    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    return loan

# Update a loan
def update_loan(db: Session, customer_id: int, loan_type: str ,loan_data: schemas.LoanUpdate):
    loan = db.query(models.Loan).filter(models.Loan.customer_id == customer_id, models.Loan.loan_type == loan_type).first()

    if loan is None:
        raise HTTPException(status_code=404, detail="Loan not found for this customer and loan type")

    loan.amount = loan_data.amount
    loan.duration_months = loan_data.duration_months
    #loan.applied_on=datetime.utcnow().now
    db.commit()  
    db.refresh(loan) 
    
    return loan
