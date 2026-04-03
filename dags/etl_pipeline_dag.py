from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

PROJECT_DIR = "/opt/airflow/project"

with DAG(
    dag_id='etl_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    bronze_task = BashOperator(
        task_id='bronze_task',
        bash_command='python /opt/airflow/project/scripts/bronze.py'
    )

    silver_task = BashOperator(
        task_id='silver_task',
        bash_command='python /opt/airflow/project/scripts/silver.py'
    )

    quality_task = BashOperator(
        task_id='quality_task',
        bash_command='python /opt/airflow/project/scripts/data_quality.py'
    )

    gold_task = BashOperator(
        task_id='gold_task',
        bash_command='python /opt/airflow/project/scripts/gold.py'
    )

    bronze_task >> silver_task >> quality_task >> gold_task