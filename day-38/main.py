import requests
from datetime import datetime
APP_ID="app id"
API_KEY="app key"
YOUR_USERNAME="username of sheety"
YOUR_PASSWORD="password of sheety"
EXERCISE_ENDPOINT="exercise endpoint"
SHEETY_ENDPOINT="url of sheety endpoint"
exercise_input=input("Tell me which exercise you did?")

headers={
    "x-app-id":"your app id",
    "x-app-key":"your api key",
}
parameters={
    "query":exercise_input,
}
#hardcoded due to signup issues
sample_response = {
    "exercises": [
        {
            "name": "running",
            "duration_min": 30,
            "nf_calories": 300
        }
    ]
}
now=datetime.now()
date=now.strftime("%d/%m/%Y")
time=now.strftime("%H:%M:%S")

for exercise in sample_response["exercises"]:
    sheet_inputs={
        "workout":{
            "date":date,
            "time":time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(
        SHEET_ENDPOINT, 
        json=sheet_inputs, 
        auth=(
            YOUR_USERNAME, 
            YOUR_PASSWORD,
        )
)
print(sheet_response.text)