from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/")
def create_transaction(data: TransactionCreate, db: Session = Depends(get_db)):
    transaction = Transaction(
        amount=data.amount,
        type=data.type,
        category=data.category,
        date=data.date,
        description=data.description
    )

    db.add(transaction)
    db.commit()

    return {"message": "Transaction added successfully"}


@router.get("/")
def get_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()