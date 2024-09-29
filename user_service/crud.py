from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import model, schemas
import re
from utils import get_password_hash, verify_password,create_full_name

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
# Function to validate contact_no
def validate_contact_no(contact_no: int) -> bool:
    if len(str(contact_no)) != 10 or not str(contact_no).isdigit():
        return False
    return True

# Function to create a new user with validations
def create_user(db: Session, user: schemas.UserCreate):
    # Check if username already exists
    existing_user = db.query(model.User).filter(model.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    existing_user_contact_no = db.query(model.User).filter(model.User.contact_no == user.contact_no).first()
    if existing_user_contact_no:
        raise HTTPException(status_code=400, detail="Contact number already registered")


    # Validate email format
    if not validate_email(user.email):
        raise HTTPException(status_code=400, detail="Invalid email format")

    # Validate password strength
    if not validate_password(user.password):
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters long")
    
    if not validate_contact_no(user.contact_no):
        raise HTTPException(status_code=400, detail="contact_no must be equal to 10 digits")

    # Hash the user's password
    hashed_password = get_password_hash(user.password)

    full_name=create_full_name(user.first_name,user.last_name)

    # Create user model object
    db_user = model.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        first_name=user.first_name,
        last_name=user.last_name,
        full_name=full_name,
        address=user.address,
        state=user.state,
        country=user.country,
        dob=user.dob,
        contact_no=user.contact_no
        #account_type=user.account_type,
    )

    # Add the user to the database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"status": "success", "message": "User created successfully"}

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


# Retrieve user by ID
def get_user(db: Session, user_id: int):
    user = db.query(model.User).filter(model.User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=400, detail="User not found")
    return user

# Retrieve all users
def get_users(db: Session):
    user = db.query(model.User).all()
    
    if user is None:
        raise HTTPException(status_code=400, detail="No Users available")
    return user

