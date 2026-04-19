import requests
import datetime

MY_LATITUDE=12.971599
MY_LONGITUDE=77.594566

location={
    "lat":MY_LATITUDE,
    "lng":MY_LONGITUDE,
    "formatted":0
}

response=requests.get(url="https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400",params=location)
data=response.json()
sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]
current=datetime.datetime.now()
current_hour=current.hour
print(current_hour)
print(sunrise)
print(sunset)