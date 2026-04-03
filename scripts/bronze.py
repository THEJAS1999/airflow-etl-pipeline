from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Bronze Layer").getOrCreate()

input_path = "/opt/airflow/project/data/orders.csv"
output_path = "/opt/airflow/project/output/bronze_orders"

df = spark.read.csv(input_path, header=True, inferSchema=True)

df.write.mode("overwrite").parquet(output_path)

spark.stop()