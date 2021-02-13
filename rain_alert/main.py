import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from env import API_KEY, MY_LAT, MY_LONG, ACCOUNT_SID, AUTH_TOKEN, FROM_PHONE, TO_PHONE

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "units": "metric",
    "exclude": "current,minutely,daily"
}

will_rain = False

response = requests.get(OWM_Endpoint, params)
response.raise_for_status()
weather_codes_next_12_hours = [hour["weather"][0]["id"] for hour in response.json()["hourly"]][:12]
for code in weather_codes_next_12_hours:
    if code < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(ACCOUNT_SID, AUTH_TOKEN, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂",
        from_=FROM_PHONE,
        to=TO_PHONE
    )

    print(message.status)
