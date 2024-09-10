from fastapi import FastAPI, Depends, HTTPException
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import model, schemas, crud

app = FastAPI()

# Create the database tables
model.Base.metadata.create_all(bind=engine)

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register/", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# Login endpoint to authenticate user
@app.post("/login/")
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    response = crud.authenticate_user(db=db, user=user)
     
    if response["status"] == "error":
        raise HTTPException(status_code=400, detail=response["message"])
    
    return response  