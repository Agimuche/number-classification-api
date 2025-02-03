import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Render!"}

if __name__ == "__main__":
    # Get the port from the environment variable
    port = int(os.environ.get("PORT", 10000))  # Default to 10000 if not set by Render
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)

from fastapi import FastAPI, Query
from typing import Dict

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Number Classification API!"}

@app.get("/classify")
def classify_number(number: int = Query(..., description="Enter an integer")) -> Dict:
    if number % 2 == 0:
        return {"number": number, "classification": "even"}
    else:
        return {"number": number, "classification": "odd"}

# Function to check if a number is prime 
def is_prime(n: int) -> bool:
    if n < 2:
        return False 
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True  # This should be outside the for loop

# Function to check if a number is perfect
def is_perfect(n: int) -> bool:
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n 

# Function to check if a number is an Armstrong number
def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

@app.get("/api/classify-number")
def classify_number(number: int = Query(..., description="Enter an integer")) -> Dict:
    try:
        # Convert input to integer
        num = int(number)
    except ValueError:  # Corrected to ValueError
        return {"number": number, "error": True}
    
    # Classify the number 
    prime = is_prime(num)
    perfect = is_perfect(num)
    armstrong = is_armstrong(num)
    odd_or_even = "odd" if num % 2 != 0 else "even"
    digit_sum = sum(int(digit) for digit in str(num))

    # Determine properties
    properties = []
    if armstrong:
        properties.append("armstrong")
    properties.append(odd_or_even)

    # Get fun fact from Number API
    fun_fact = "No fun fact found"
    try: 
        response = requests.get(f"http://numbersapi.com/{num}/math")
        if response.status_code == 200:
            fun_fact = response.text
    except Exception:
        pass 

    # Return JSON response
    return {
        "number": num,
        "is_prime": prime,
        "is_perfect": perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }
