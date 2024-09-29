import uuid

def generate_unique_no(loan_type: str) -> str:
    prefix = ""
    if loan_type == "Personal":
        prefix = "PL"
    elif loan_type == "Home":
        prefix = "HL"
    elif loan_type == "Car":
        prefix = "CL"
    unique_no = f"{prefix}{uuid.uuid4().hex[:8].upper()}"
    return unique_no


def validate_amount(amount: int) -> bool:
    if amount > 10000 and amount < 10000000:
        return True
    return False

def validate_duration_months(duration_months: int) -> bool:
    if duration_months >24 or duration_months==24:
        return True
    return False
