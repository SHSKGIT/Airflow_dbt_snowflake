from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import os


default_args = {
    'owner': 'jerrywang',
    'depends_on_past': False,
    'start_date': datetime(2024,5,27),
    'retries': 0
}

with DAG('transformation_analysis_dag', default_args=default_args, schedule_interval='@once') as dag:
    task_transform = BashOperator(
        task_id='transform',
        bash_command='cd /jerrywang_dbt_project && dbt run --models transform --profiles-dir .',
        env={
            'dbt_user': '{{ var.value.dbt_user }}',
            'dbt_password': '{{ var.value.dbt_password }}',
            **os.environ,
        },
        dag=dag
    )

    task_analysis = BashOperator(
        task_id='analysis',
        bash_command='cd /jerrywang_dbt_project && dbt run --models analysis --profiles-dir .',
        env={
            'dbt_user': '{{ var.value.dbt_user }}',
            'dbt_password': '{{ var.value.dbt_password }}',
            **os.environ,
        },
        dag=dag
    )

    task_transform >> task_analysis

