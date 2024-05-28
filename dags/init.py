from datetime import datetime
import os

from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'jerrywang',
    'depends_on_past': False,
    'start_date': datetime(2024,5,27),
    'retries': 0,
}

with DAG('init_dag', default_args=default_args, schedule_interval='@once') as dag:
    task_init = BashOperator(
        task_id='load_seed_data_once',
        bash_command='cd /jerrywang_dbt_project && dbt seed --profiles-dir .',  # load csv files into a data warehouse
        env={
            'dbt_user': '{{ var.value.dbt_user }}',
            'dbt_password': '{{ var.value.dbt_password }}',
            **os.environ,
        },
        dag=dag
    )

    task_init

