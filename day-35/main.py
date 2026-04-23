import requests
import smtplib

my_email=ur_email
my_password=app_password

OWM_Endpoint = " https://api.openweathermap.org/data/2.5/forecast"
api_key="0d87c6de1001ef06dc98c1c65c53a829"

weather_params={
    "lat":12.971599,
    "lon":77.594566,
    "appid":api_key,
    "cnt":4,
}
response=requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data=response.json()
will_rain=False
for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com",587)as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs="rithishtestemail@yahoo.com",
                            msg=f"Subject:Rain alert!\n\nCarry an ubrella")
    print("carry an umbrella")
