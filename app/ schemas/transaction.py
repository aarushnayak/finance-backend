from datetime import date
from typing import Optional
from pydantic import BaseModel


class TransactionCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    description: Optional[str] = None