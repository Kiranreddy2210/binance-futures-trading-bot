from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET")
)

client.FUTURES_URL = "https://demo-fapi.binance.com"
def get_client():
    return client

print("API Loaded:", bool(os.getenv("API_KEY")))
print("Secret Loaded:", bool(os.getenv("API_SECRET")))