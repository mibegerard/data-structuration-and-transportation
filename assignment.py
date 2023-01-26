import requests
from datetime import date
from datetime import datetime
from time import mktime
from collections import Counter
from airflow.decorators import dag, task

BASE_URL = "https://opensky-network.org/api"

def to_seconds_since_epoch(input_date: str) -> int:
  return int(mktime(date.fromisoformat(input_date).timetuple()))

params = {
    "airport": "LFPG", # ICAO code for CDG
    "begin": to_seconds_since_epoch("2022-12-01"),
    "end": to_seconds_since_epoch("2022-12-02")
}

cdg_flights = f"{BASE_URL}/flights/departure"

@dag(

    schedule=None,
    start_date=datetime(2023, 1, 11 ),
    catchup=False
)
    
def assignment1():

    @task
    def read_flights(url: str) -> str:
      response = requests.get(cdg_flights, params=params)
      flights = response.json()
      counter = Counter([flight["estArrivalAirport"] for flight in flights if (flight["estArrivalAirport"] is not None and flight["estArrivalAirport"] != "LFPG")])
      print(counter.most_common(1))

_ = assignment1()
