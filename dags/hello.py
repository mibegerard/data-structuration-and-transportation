from airflow.decorators import dag, task
from datetime import datetime

@dag(
    schedule=None,
    start_date=datetime(2023, 1, 11),
    catchup=False
)
def hello_dag():
    
    @task
    def say_hello() -> str:
      return "Hello, world!"

    hello = say_hello()

_ = hello_dag()