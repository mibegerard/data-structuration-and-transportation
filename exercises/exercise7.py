import json
from collections import defaultdict

FILE_PATH = "resources/json/french-cities.json" 

with open(FILE_PATH, "r") as f:
  data = json.load(f)

regions = defaultdict(list)

for row in data:
  regions[row['admin_name']].append(row)
   

def compute_data_for_region(cities) -> tuple[int, int, str]:
    populations = [int(city['population']) for city in cities if city['population'] != '']
    biggest_city = max(cities, key=lambda x: int(x['population']) if x['population'] != '' else 0)
    return (sum(populations), int(sum(populations) / len(populations)), biggest_city['city'])

for region in regions:
   print(compute_data_for_region(regions[region]))