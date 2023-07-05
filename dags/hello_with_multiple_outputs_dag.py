from typing import Dict
from airflow.decorators import dag, task
from datetime import datetime

@dag(
    schedule=None,
    start_date=datetime(2023, 1, 11),
    catchup=False
)
def hello_with_multiple_outputs_dag():

    @task(multiple_outputs=True)
    def give_names() -> Dict:
      return {"names": ["Pierre", "Ada"]}
    
    @task
    def say_hello(names: Dict):
      for name in names["names"]:
        print(name)

    names = give_names()
    hello = say_hello(names)

_ = hello_with_multiple_outputs_dag()