from airflow.decorators import dag, task
from datetime import datetime

@dag(
    schedule=None,
    start_date=datetime(2023, 1, 11),
    catchup=False
)
def hello_with_parameters_dag():
    
    @task
    def say_hello(name: str) -> str:
      return f"Hello, world! My name is {name}"
    
    @task()
    def my_task_name(ds=None):
      return ds # should return 2023-01-21

    hello = say_hello("Pierre")

    my_task = my_task_name()

    hello >> my_task

_ = hello_with_parameters_dag()