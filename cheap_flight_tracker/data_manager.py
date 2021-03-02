from env import SHEETY
import requests


class DataManager:

    def __init__(self):
        self.endpoint_prices = f"https://api.sheety.co/{SHEETY['api_key']}{SHEETY['prices_url']}"
        self.endpoint_users = f"https://api.sheety.co/{SHEETY['api_key']}{SHEETY['users_url']}"
        self.headers = {"Authorization": SHEETY["bearer"]}

    def get_data(self):
        """Returns Json of stored data in google spread sheet"""
        response = requests.get(url=self.endpoint_prices, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def post_data(self, data):
        """Saves data into new row (data) in google spread sheet"""
        response = requests.post(url=self.endpoint_prices, json=data, headers=self.headers)
        response.raise_for_status()

    def put_data(self, data, object_id):
        """Alters an entry (data) in a specific row (object_id) in google spread sheet"""
        response = requests.put(url=f"{self.endpoint_prices}/{object_id}", json=data, headers=self.headers)
        response.raise_for_status()

    def get_users(self):
        """Returns Json of stored user in google spread sheet"""
        response = requests.get(url=self.endpoint_users, headers=self.headers)
        response.raise_for_status()
        return response.json()