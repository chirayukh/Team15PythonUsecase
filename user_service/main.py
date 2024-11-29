from fastapi import FastAPI, Depends, HTTPException,status
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import model, schemas, crud
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

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
# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")        

@app.post("/register/",status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# Login endpoint to authenticate user
@app.post("/login/")
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    response = crud.authenticate_user(db=db, user=user)
     
    if response["status"] == "error":
        raise HTTPException(status_code=400, detail=response["message"])
    
    return response  

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db=db, user_id=user_id)

@app.get("/users/")
def get_users(db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    return crud.get_users(db=db, token=token)


@app.put("/users/{user_id}")
def update_user(user_id: int,user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user_id=user_id,user_update=user_update)