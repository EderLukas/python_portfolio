import requests
from datetime import datetime
from env import TOKEN, USERNAME, GRAPH_ID


pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(endpoint_pixela, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "minute",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now().strftime("%Y%m%d")
pixel_config = {
    "date": today,
    "quantity": "95",
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

pixel_update_config = {
    "quantity": "95",
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)