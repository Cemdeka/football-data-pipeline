import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_FOOTBALL_KEY")

url = "https://v3.football.api-sports.io/status"

headers = {
    "x-apisports-key": API_KEY
}

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)
print(response.json())
