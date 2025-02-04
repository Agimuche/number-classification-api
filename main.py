from fastapi import FastAPI, Query
from pydantic import BaseModel, EmailStr
import requests
from typing import Dict
from datetime import datetime
from math import sqrt

app = FastAPI()

GITHUB_URL = "https://github.com/Agimuche/number-classification-api"
EMAIL = "Agimuche1@gmail.com"  # Ensure this is a valid email format

# Function to check if a number is prime
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is perfect
def is_perfect(n: int) -> bool:
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

# Function to check if a number is an Armstrong number
def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

# Response model for validation
class NumberClassificationResponse(BaseModel):
    number: int
    is_prime: bool
    is_perfect: bool
    properties: list
    digit_sum: int
    fun_fact: str
    current_datetime: str
    github_url: str
    email: EmailStr

# Root endpoint to welcome users
@app.get("/")
def read_root():
    return {"message": "Welcome to the Number Classification API"}

@app.get("/api/classify-number", response_model=NumberClassificationResponse)
def classify_number(number: int = Query(..., description="Enter an integer")):
    # Classify the number
    prime = is_prime(number)
    perfect = is_perfect(number)
    armstrong = is_armstrong(number)
    odd_or_even = "odd" if number % 2 != 0 else "even"
    digit_sum = sum(int(digit) for digit in str(number))

    # Determine properties
    properties = []
    if armstrong:
        properties.append("armstrong")
    properties.append(odd_or_even)

    # Get fun fact from Numbers API
    fun_fact = "No fun fact found"
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math")
        if response.status_code == 200:
            fun_fact = response.text
    except Exception:
        pass

    # Return JSON response with validated fields
    return NumberClassificationResponse(
        number=number,
        is_prime=prime,
        is_perfect=perfect,
        properties=properties,
        digit_sum=digit_sum,
        fun_fact=fun_fact,
        current_datetime=datetime.utcnow().isoformat(),
        github_url=GITHUB_URL,
        email=EMAIL
    )
