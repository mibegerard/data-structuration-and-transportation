import json
import sqlite3
from dataclasses import astuple, dataclass

FILE_PATH = "resources/json/users.json" 

@dataclass
class User:
  id: str
  name: str
  city: str
  school: str
  age: int
  is_teacher: bool

def build_user(input_dict) -> User:
  return User(
    id=input_dict["id"],
    name=input_dict["name"],
    city=input_dict["city"],
    school=input_dict["school"],
    age=input_dict["age"],
    is_teacher=input_dict["is_teacher"]
  )

with open(FILE_PATH, "r") as f:
  data = json.load(f)
  users = [astuple(build_user(row)) for row in data]

connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE users (id text, name text, city text, school text, age int, is_teacher int)")
connection.executemany("INSERT INTO users VALUES(?, ?, ?, ? ,?, ?)", users)
connection.commit()
res = connection.execute("SELECT * FROM users")

for row in res:
  print(row)