import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
OWM_API_KEY = os.environ.get("OWM_API_KEY")

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

weather_params = {
    "lat": 32.099491,
    "lon": 34.955341,
    "appid": OWM_API_KEY,
    "cnt": 4,
}

TWILIO_PHONE = os.environ.get("TWILIO_PHONE")
MY_PHONE = os.environ.get("MY_PHONE")

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
twelve_stamp = data["list"]
will_rain = False
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
for i in twelve_stamp:
    _id = i["weather"][0]['id']
    if _id < 700:
        will_rain = True
if will_rain:
    message_body = "It's going to rain today. Remember to bring an umbrella ☂️"
else:
    message_body = "Sky looks clear have a nice day."

message = client.messages.create(
    from_=TWILIO_PHONE,
    body=message_body,
    to=MY_PHONE
)
