import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 47.421051
MY_LONG = 8.305380


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and \
            MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour
    #If the ISS is close to my current position
    # and it is currently dark
    if current_hour <= sunrise or current_hour >= sunset:
        return True


# Then send me an email to tell me to look up.
my_email = "AdlvowicmMN3@gmail.com"
my_pass = "Zf7gMgaV5Cpz6py"

while True:
    time.sleep(60)
    if is_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(from_addr=my_email,
                                to_addrs="eder.lukas@bluewin.ch",
                                msg="Subject:ISS-Tracker\n\n"
                                    "The ISS is currently in your night sky\n"
                                    "Best wishes\n"
                                    "Tracker-Bot")

# BONUS: run the code every 60 seconds.



