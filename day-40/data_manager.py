import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT="https://api.sheety.co/67caa158f9c0fd125abbccbd1b2cf45c/myFlightDeals/prices"
class DataManager:
    def __init__(self):
        self._user=os.environ["SHEETY_USERNAME"]
        self._password=os.environ["SHEETY_PASSWORD"]
        self._authorization=HTTPBasicAuth(self._user,self._password)
        self.destination_data={}

    def get_destination_data(self):
        response=requests.get(url=SHEETY_ENDPOINT,auth=self._authorization)
        data=response.json()
        self.destination_data=data["prices"]
        return self.destination_data
    
    def update_lowest_price(self,row_id,new_price):
        new_data={
            "price":{
                "lowestPrice":new_price
            }
        }
        requests.put(
            url=f"{SHEETY_ENDPOINT}/{row_id}",
            json=new_data,
            auth=self._authorization,
        )
    def get_customers_emails(self):
        user_response=requests.get(url=os.environ["USERS_SHEET"],auth=self._authorization)
        data=user_response.json()
        self.user_data=data["users"]
        return self.user_data
