from datetime import datetime, timedelta
import json
from flight_search import FlightSearch


ORIGIN_CITY_IATA = "LON"

data = json.load(open("flights.json"))

for flight in data:
    if flight["iata_code"] == "":
        flight["iata_code"] = FlightSearch(
        ).get_destination_code(flight["city"])
        print(f"{flight['city']}: {flight['iata_code']}")

with open("flights.json", "w") as data_file:
    json.dump(data, data_file, indent=4)

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6*30))

for destination in data:
    flight = FlightSearch().check_flights(
        ORIGIN_CITY_IATA,
        destination["iata_code"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
