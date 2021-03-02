from env import TEQUILA
import requests
import datetime as dt
from flight_data import FlightData
import pprint as pp


class FlightSearch:

    def __init__(self):
        self.endpoint = "https://tequila-api.kiwi.com/"
        self.headers = {"apikey": TEQUILA["api_key"]}

    def get_iata_code_by_city(self, city):
        """Searches iata codes for city names and returnes the iata"""
        body = {
            "term": city,
            "locale": "en-US",
            "location_types": "city",
        }
        response = requests.get(url=f"{self.endpoint}locations/query", params=body,
                                headers=self.headers)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def search_a_flight(self, destination):
        """searches flight to given destination"""
        tomorrow = (dt.datetime.now() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
        tomorrow_plus_six_months = (dt.datetime.now() + dt.timedelta(days=180)).strftime("%d/%m/%Y")
        earliest_return = (dt.datetime.now() + dt.timedelta(days=7)).strftime("%d/%m/%Y")
        latest_return = (dt.datetime.now() + dt.timedelta(days=208)).strftime("%d/%m/%Y")
        body = {
            "fly_from": "LON",
            "fly_to": destination,
            "date_from": tomorrow,
            "date_to": tomorrow_plus_six_months,
            "return_from": earliest_return,
            "return_to": latest_return,
            "nights_in_dst_from": 1,
            "nights_in_dst_to": 27,
            "flight_type": "round",
            "selected_cabins": "M",
            "adult_hold_bag": [1],
            "adult_hand_bag": [1],
            "curr": "GBP",
            "locale": "en",
            "max_stopovers": 0,
        }
        response = requests.get(url=f"{self.endpoint}v2/search", params=body, headers=self.headers)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            body["max_stopovers"] = 1
            response = requests.get(url=f"{self.endpoint}v2/search", params=body, headers=self.headers)
            response.raise_for_status()
            data = response.json()["data"][0]
            pp.pprint(data)
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["cityFrom"],
                origin_airport=data["flyFrom"],
                destination_city=data["cityTo"],
                destination_airport=data["flyTo"],
                out_date=data["local_departure"].split("T")[0],
                return_date=data["local_departure"].split("T")[0]
            )

            return flight_data

        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["cityFrom"],
                origin_airport=data["flyFrom"],
                destination_city=data["cityTo"],
                destination_airport=data["flyTo"],
                out_date=data["local_departure"].split("T")[0],
                return_date=data["local_departure"].split("T")[0]
            )

            return flight_data

