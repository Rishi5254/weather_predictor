import requests
from twilio.rest import Client
import datetime as dt

account_sid = "ACb6e24d33a95f3116e3a8ae96afc7e971"
auth_token = "e4fd5b9ce4c6738534a295f57f749f86"
client = Client(account_sid, auth_token)

def rain_check():
    api_id ="42f9c2cd0947d6958ffb2cd0ff34d98a"

    parameters = {
        "lat": 18.790894,
        "lon": 78.911850,
        "exclude": "current,minutely,daily,alerts",
        "appid": api_id,
    }
    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    response.raise_for_status()
    data = response.json()
    slice_data = data["hourly"][:12]

    for each in slice_data:
        new = each['weather'][0]["id"]
        if new < 700:
            return "Bring Umbrella"




if  rain_check():
    message = client.messages \
        .create(
        body="Carry a  Umbrellela it might Rain Today ☔ ",
        from_ ='+19283994204',
        to='+918143222173'
    )
    print(message.status)