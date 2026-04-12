from fastapi import FastAPI

from app.database import Base, engine
from app.routes.auth import router as auth_router
from app.routes.transaction import router as transaction_router
from app.routes.summary import router as summary_router

from app.models import user, transaction

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance Backend")


@app.get("/")
def home():
    return {"message": "Finance Backend Running"}


app.include_router(auth_router)
app.include_router(transaction_router)
app.include_router(summary_router)
