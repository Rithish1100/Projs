import requests_cache
from data_manager import DataManager
from pprint import pprint
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager
from dotenv import load_dotenv
import os

load_dotenv()
requests_cache.install_cache("flight_cache",
urls_expire_after={
    "*.sheety.co*":requests_cache.DO_NOT_CACHE,
    "*":3600,
}
)
data_manager=DataManager()
flight_search=FlightSearch()
notification_manager=NotificationManager()
sheet_data=data_manager.get_destination_data()
now=datetime.now()
tomorrow=now+timedelta(days=1)
six_months_from_today=now+relativedelta(months=6)

ORIGIN_CITY_IATA="BLR"
for destination in sheet_data:
    city=destination["city"]
    pprint(f"Getting flights for {city}")
    flights=flight_search.check_flights(
        ORIGIN_CITY_IATA,destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today)

# pprint(flight_data)
# pprint(sheet_data)
    cheapest_flight=find_cheapest_flight(flights,return_date=six_months_from_today.strftime("%Y-%m-%d"))
    pprint(f"{city}:GBP{cheapest_flight.price}")

    if cheapest_flight.price!="N/A" and cheapest_flight.price<destination["lowestPrice"]:
        pprint(f"lower price flight found to{destination['city']}!")
        data_manager.update_lowest_price(destination["id"],cheapest_flight.price)
        notification_manager.send_email(to_email=os.environ["RECEIVER_EMAIL"],
                                        subject="Flight price offer",
                                        body=f"Low price alert! only GBP{cheapest_flight.price}to fly"
                                             f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport},"
                                             f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")