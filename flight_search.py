import requests
from flight_data import FlightData
import os
from dotenv import load_dotenv

load_dotenv()

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")
