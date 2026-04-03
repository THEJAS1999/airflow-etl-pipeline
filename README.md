# airflow-etl-pipeline

A simple Apache Airflow ETL pipeline that processes raw order data through bronze, silver, and gold stages.

## Project Overview

This repository contains an Airflow DAG and Python ETL scripts for a staged data pipeline:

- `dags/etl_pipeline_dag.py`: Defines the Airflow DAG and task dependencies.
- `scripts/bronze.py`: Loads raw data into the bronze layer.
- `scripts/silver.py`: Transforms bronze data into the silver layer.
- `scripts/data_quality.py`: Runs data quality checks on the silver output.
- `scripts/gold.py`: Aggregates final metrics into the gold layer.
- `data/orders.csv`: Sample source data.
- `output/bronze_orders/`, `output/silver_orders/`, `output/gold_product_sales/`: Processed outputs.

## DAG Flow

The DAG `etl_pipeline` runs tasks in this order:

1. `bronze_task`
2. `silver_task`
3. `quality_task`
4. `gold_task`

## Usage

1. Place the project under your Airflow home or mount it in the Airflow container.
2. Ensure the `dags` folder is available to the Airflow scheduler.
3. Start Airflow scheduler and webserver.
4. Trigger the `etl_pipeline` DAG from the Airflow UI or wait for the scheduled run.

## Execution Details

The DAG uses `BashOperator` commands to execute the scripts from `/opt/airflow/project`:

- `python /opt/airflow/project/scripts/bronze.py`
- `python /opt/airflow/project/scripts/silver.py`
- `python /opt/airflow/project/scripts/data_quality.py`
- `python /opt/airflow/project/scripts/gold.py`

## Notes

- Update the path in `dags/etl_pipeline_dag.py` if your Airflow project root differs from `/opt/airflow/project`.
- This pipeline is configured with `catchup=False` and runs daily.

## Author

Thejas P Y
Data Engineering

GitHub: <https://github.com/THEJAS1999>
LinkedIn: <https://linkedin.com/in/thejasyatheendran>