from datetime import datetime

from airflow.decorators import dag, task
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.sqlite.hooks.sqlite import SqliteHook

@dag(
    schedule=None,
    start_date=datetime(2023, 1, 11),
    catchup=False
)
def exercise18():

  @task()
  def insert_with_hook():
    sqlite_hook = SqliteHook()
    rows = [("0001", "Pierre", "Paris", "EPITA" , 36, 1), ("0002", "Ada", "Boston", "Home", 27, 0)]
    target_fields = ['id', 'name', 'city', 'school', 'age', 'is_teacher']
    sqlite_hook.insert_rows(table='users', rows=rows, target_fields=target_fields)

  drop_table = SqliteOperator(task_id="drop_table", sql="sql/drop_table.sql")

  create_table = SqliteOperator(task_id="create_table", sql="sql/create_table.sql")

  add_data = insert_with_hook()

  drop_table >> create_table >> add_data

_ = exercise18()