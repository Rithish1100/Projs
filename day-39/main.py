import requests_cache
from data_manager import DataManager
from pprint import pprint
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

requests_cache.install_cache("flight_cache",
urls_expire_after={
    "*.sheety.co*":requests_cache.DO_NOT_CACHE,
    "*":3600,
}
)
data_manager=DataManager()
flight_search=FlightSearch()
sheet_data=data_manager.get_destination_data()
now=datetime.now()
tommorow=now+timedelta(days=1)
six_months_from_today=now+relativedelta(months=6)

ORIGIN_CITY_IATA="BLR"
for destination in sheet_data:
    pprint(f"Getting flights for{destination['city']}")
    flights=flight_search.check_flights(
        ORIGIN_CITY_IATA,destination["iataCode"],
        from_time=tommorow,
        to_time=six_months_from_today)

# pprint(flight_data)
# pprint(sheet_data)
    cheapest_flight=find_cheapest_flight(flights,return_date=six_months_from_today.strftime("%Y-%m-%d"))
    pprint(f"{destination['city']}:GBP{cheapest_flight.price}")

    if cheapest_flight.price!="N/A" and cheapest_flight.price<destination["lowestPrice"]:
        pprint(f"lower price flight found to{destination['city']}!")
        data_manager.update_lowest_price(destination["id"],cheapest_flight.price)