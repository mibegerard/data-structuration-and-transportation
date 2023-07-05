from airflow.decorators import dag
from airflow.operators.python import PythonOperator
from datetime import datetime

@dag(
    schedule=None,
    start_date=datetime(2023, 1, 11),
    catchup=False
)
def hello_operator_with_relations_dag():
    
    def say_hello() -> str:
      return "Hello, world!"
    
    hello = PythonOperator(task_id="hello", python_callable=say_hello)

    hello_again = PythonOperator(task_id="hello_again", python_callable=say_hello)

    hello >> hello_again

_ = hello_operator_with_relations_dag()