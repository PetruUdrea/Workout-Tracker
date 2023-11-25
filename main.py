import requests
import datetime as dt
import os

APP_ID = os.environ.get("NT_APP_ID")  # put your APP_ID here from the nutritionix api
API_KEY = os.environ.get("NT_API_KEY")  #put your API_KEY here from the nutritionix api      
GENDER = "male"
WEIGHT_KG = 71.5  # here type your weight as a float number
HEIGHT_CM = 180.65 # type your height as a float number
AGE = 23 # type your age as an integer
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")  # put your token from the sheety api

nutrinionix_endpoint = "https://trackapi.nutritionix.com"
exercise_enpoint = f"{nutrinionix_endpoint}/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": input("What exercise have you done today? "),  # here you can use natural language ex: I ran 3 miles
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

nutrition_response = requests.post(url=exercise_enpoint, json=params, headers=headers)
result = nutrition_response.json()

sheety_endpoint = "https://api.sheety.co/2a5e1b8d143a0622550e3c5c1a34aac1/copyOfMyWorkouts/workouts" # here use your own endpoint from sheety
today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

sheety_headers = {
    "Authorization": SHEETY_TOKEN,
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    #Adding a new row in my sheets
    sheety_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=sheety_headers)

    print(sheety_response.text) # here you can see the results in a json format, and if you will go to your google sheet you will
                                # the exact same values but easier to read formatted.


