from fastapi import FastAPI, Query, HTTPException
import requests
from typing import Dict
from datetime import datetime
from math import sqrt

app = FastAPI()

GITHUB_URL = "https://github.com/Agimuche/number-classification-api"
EMAIL = "Agimuche1@gmail.com"  # Change this to your real email

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

@app.get("/api/classify-number")
def classify_number(number: int = Query(..., description="Enter an integer")) -> Dict:
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
        else:
            fun_fact = f"Error fetching fun fact: {response.status_code}"
    except requests.exceptions.RequestException as e:
        fun_fact = f"Error fetching fun fact: {e}"

    # Return JSON response
    return {
        "number": number,
        "is_prime": prime,
        "is_perfect": perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact,
        "current_datetime": datetime.utcnow().isoformat(),
        "github_url": GITHUB_URL,
        "email": EMAIL
    }
