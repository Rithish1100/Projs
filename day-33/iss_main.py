import requests
from datetime import datetime
import smtplib
import time

MY_LAT =  -14.971599 # Your latitude
MY_LONG = 73.594566 # Your longitude
MY_EMAIL="rithishtest@gmail.com"
MY_PASSWORD="hgh jhh jhhj"
latitude=0.00
longitude=0.00

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

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
current_hour=time_now.hour

while True:
    time.sleep(60)
    if ((iss_latitude>=MY_LAT and iss_latitude <=MY_LAT+5) or (iss_latitude<=MY_LAT and iss_latitude>=MY_LAT-5)) and ((iss_longitude>=MY_LONG and iss_longitude <=MY_LONG+5) or (iss_longitude<=MY_LONG and iss_longitude>=MY_LONG-5)):
        if current_hour>sunset or current_hour<sunrise:
            with smtplib.SMTP("smtp.gmail.com",587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL,password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,to_addrs="rithishtestemail@yahoo.com",msg="Subject:Lookup\n\niss is near by")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



