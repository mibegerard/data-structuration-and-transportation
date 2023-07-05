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
  users = [build_user(row) for row in data]

def adapt_user(user: User) -> str:
  values = [str(value) for value in list(astuple(user))]
  return ";".join(values)

def convert_user(user_from_db) -> User:
    id, name, city, school, age, is_teacher = [el.decode("utf8") for el in user_from_db.split(b";")]
    return User(id, name, city, school, int(age), bool(is_teacher))

sqlite3.register_adapter(User, adapt_user)
sqlite3.register_converter("user", convert_user)
connection = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
connection.execute("CREATE TABLE users (user_data user)")
connection.executemany("INSERT INTO users VALUES(?)", [(user,) for user in users])
connection.commit()
res = connection.execute("SELECT * FROM users")

for row in res:
  print(row)