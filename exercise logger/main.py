import requests
from datetime import datetime

# Nutritionix API credentials (Replace with your actual APP ID and API KEY)
APP_ID = "your APP ID"  # Nutritionix App ID
API_KEY = "your API KEY"  # Nutritionix API Key

# Nutritionix API endpoint for natural language exercise logging
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Sheety API endpoint (Replace with your actual Sheety POST endpoint)
sheety_endpoint = "your sheety post endpoint"

# Headers for Nutritionix API request
user_params = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

# Taking user input for the exercise performed
exercise = {
    "query": input("What exercise did you do today? ")
}

# Sending POST request to Nutritionix API to retrieve exercise details
nutrition_NL_response = requests.post(url=nutritionix_endpoint, headers=user_params, json=exercise)

# Extracting current date and time
date_today = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

# Preparing data for Sheety API with exercise details returned by Nutritionix API
spreadsheet_data = {
    "workout": {
        "date": date_today,
        "time": time_now,
        "exercise": nutrition_NL_response.json()["exercises"][0]["name"].title(),  # Capitalize exercise name
        "duration": nutrition_NL_response.json()["exercises"][0]["duration_min"],  # Duration of exercise in minutes
        "calories": nutrition_NL_response.json()["exercises"][0]["nf_calories"]  # Calories burned
    }
}

# Headers for Sheety API request, including Authorization token (Replace with your Sheety Basic Auth token)
sheety_header = {
    "Authorization": "your basic auth token"
}

# Sending POST request to Sheety to log exercise data in a spreadsheet
sheety_response = requests.post(url=sheety_endpoint, headers=sheety_header, json=spreadsheet_data)

# Printing Sheety API response
print(sheety_response.text)
