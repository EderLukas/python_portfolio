from env import NUTRITIONIX_HEADERS, NUTRITIONIX_REQUEST, SHEETY_KEY, SHEETY_BEARER
import requests
from datetime import datetime

NUTRITIONIX_EXERCISE_ENDPOINT = " https://trackapi.nutritionix.com/v2/natural/exercise"


def main():
    # Get activity from user.
    exercise_query = input("Tell me which exercises you did: ")
    NUTRITIONIX_REQUEST["query"] = exercise_query
    # Get div. infos from nutritionix endpoint
    response_nutritionix = requests.post(url=NUTRITIONIX_EXERCISE_ENDPOINT,
                                         json=NUTRITIONIX_REQUEST,
                                         headers=NUTRITIONIX_HEADERS)

    # save information to spreadsheet
    date_today = datetime.now().strftime("%d/%m/%Y")
    time_now = datetime.now().strftime("%H:%M:%S")
    exercise = response_nutritionix.json()["exercises"][0]["name"]
    duration = response_nutritionix.json()["exercises"][0]["duration_min"]
    calories = response_nutritionix.json()["exercises"][0]["nf_calories"]

    body = {
        "workout": {
            "date": date_today,
            "time": time_now,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

    headers = {
        "Authorization": f"Bearer {SHEETY_BEARER}"
    }

    SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_KEY}/myWorkouts/workouts"

    response_sheety = requests.post(url=SHEETY_ENDPOINT, json=body, headers=headers)


if __name__ == '__main__':
    main()
