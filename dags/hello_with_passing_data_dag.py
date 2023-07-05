from airflow.decorators import dag, task
from datetime import datetime

@dag(
    schedule=None,
    start_date=datetime(2023, 1, 11),
    catchup=False
)
def hello_with_passing_data_dag():

    @task
    def give_name() -> str:
      return "Pierre"
    
    @task
    def say_hello(name: str) -> str:
      return f"Hello, world! My name is {name}"

    name = give_name()
    hello = say_hello(name)

_ = hello_with_passing_data_dag()