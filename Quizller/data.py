import requests

# Fetches a set of trivia questions from the Open Trivia Database API.
parameters = {
    "amount": 150,
    "type": "boolean"  # Specifies that the questions should be True/False type.
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()  # Raises an error if the API request fails.
data = response.json()
question_data = data["results"]  # Extracts the list of questions from the API response.