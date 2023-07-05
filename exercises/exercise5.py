import csv
from dataclasses import dataclass

FILE_PATH = "resources/csv/ratp.csv" 

@dataclass
class Station:
  rank: int
  network: str
  name: str
  number_of_users: int
  connections: list[str]
  city: str
  district: int | None

def parse_row(line: list[str]) -> Station:
  rank, network, name, number_of_users, connection1, connection2, connection3, connection4, connection5, city, district = line

  connections = [connection1, connection2, connection3, connection4, connection5]
  connections = [conn for conn in connections if conn != '']

  if district == '':
    district = None
  else:
    district = int(district)

  return Station(int(rank), network, name, int(number_of_users), connections, city, district)


with open(FILE_PATH, "r") as f:
  reader = csv.reader(f, delimiter=";")
  # skip the header
  next(reader, None)
  stations = [parse_row(row) for row in reader]

for station in stations:
  print(station)