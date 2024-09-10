from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import model, schemas
import re
from utils import get_password_hash, verify_password

#def create_user(db: Session, user: schemas.UserCreate):
 #   hashed_password = get_password_hash(user.password)
  #  db_user = model.User(username=user.username, email=user.email, hashed_password=hashed_password, full_name=user.full_name)
   # db.add(db_user)
    #db.commit()
    #db.refresh(db_user)
    #return db_user

# Function to validate email format
def validate_email(email: str) -> bool:
    # Basic regex for validating an email
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email) is not None

# Function to validate password strength
def validate_password(password: str) -> bool:
    if len(password) < 8:
        return False
    # You can add more complexity checks if needed (e.g., must contain digits, special characters, etc.)
    return True

# Function to create a new user with validations
def create_user(db: Session, user: schemas.UserCreate):
    # Check if username already exists
    existing_user = db.query(model.User).filter(model.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Validate email format
    if not validate_email(user.email):
        raise HTTPException(status_code=400, detail="Invalid email format")

    # Validate password strength
    if not validate_password(user.password):
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters long")

    # Hash the user's password
    hashed_password = get_password_hash(user.password)

    # Create user model object
    db_user = model.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name
        # Assign other fields as necessary
        #name=user.name,
        #address=user.address,
        #country=user.country,
        #dob=user.dob,
        #account_type=user.account_type,
    )

    # Add the user to the database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"status": "success", "message": "User created successfully", "user": db_user}

# Function to authenticate user
def authenticate_user(db: Session, user: schemas.UserLogin):
    # Fetch user by username
    db_user = db.query(model.User).filter(model.User.username == user.username).first()
    
    # Check if user exists
    if not db_user:
        return {"status": "error", "message": "Invalid username"}

    # Verify the password
    if not verify_password(user.password, db_user.hashed_password):
        return {"status": "error", "message": "Invalid password"}

    # If username and password are valid, return the user details
    return {"status": "success", "message": "User authenticated", "user": db_user}