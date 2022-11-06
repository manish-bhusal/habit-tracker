import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAMEE")
TOKEN = os.getenv("TOKENN")
GRAPH_ID = os.getenv("GRAPH_IDD")


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/{GRAPH_ID}"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


now = datetime(year=2022, month=11, day=4).strftime('%Y%m%d')

pixel_data = {
    "date": now,
    "quantity": "2.8"
}


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=pixel_creation_endpoint,
                         json=pixel_data, headers=headers)

print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{now}"

new_pixel_data = {
    "quantity": "65.3"
}

# response = requests.put(
#     url=pixel_update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{now}"


# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
