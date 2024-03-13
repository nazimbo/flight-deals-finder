from datetime import datetime, timedelta
import json
from flight_search import FlightSearch


ORIGIN_CITY_IATA = "GNB"

data = json.load(open("flights.json"))

print(data)

for flight in data:
    if flight["iata_code"] == "":
        flight["iata_code"] = FlightSearch(
        ).get_destination_code(flight["city"])

print(data)
