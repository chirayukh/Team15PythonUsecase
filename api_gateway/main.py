from fastapi import FastAPI
import requests

app = FastAPI()

USER_SERVICE_URL = "http://localhost:8001"
LOAN_SERVICE_URL = "http://localhost:8002"
ACCOUNT_SERVICE_URL = "http://localhost:8003"

@app.post("/register/")
def register_user(user: dict):
    response = requests.post(f"{USER_SERVICE_URL}/register/", json=user)
    return response.json()

@app.post("/login/")
def login_user(user: dict):
    response = requests.post(f"{USER_SERVICE_URL}/login/", json=user)
    return response.json()

@app.post("/apply-loan/")
def apply_loan(loan: dict):
    response = requests.post(f"{LOAN_SERVICE_URL}/apply-loan/", json=loan)
    return response.json()

@app.put("/update-account/{account_id}")
def update_account(account_id: int, account: dict):
    response = requests.put(f"{ACCOUNT_SERVICE_URL}/update-account/{account_id}", json=account)
    return response.json()