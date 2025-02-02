# number-classification-api
This program helps in classification of numbers into different category 
# Number Classification API (HNG12 Stage 1)

This is a public API that classifies numbers and provides interesting properties.

## API Endpoint

- **Base URL:** `https://number-classification-api.onrender.com/`
- **Method:** `GET`
- **Example:** `/api/classify-number?number=371`

### Example Response

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

