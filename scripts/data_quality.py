from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Data Quality").getOrCreate()

input_path = "/opt/airflow/project/output/silver_orders"

df = spark.read.parquet(input_path)

print("Total records:", df.count())

print("Duplicate Orders:")
df.groupBy("order_id").count().filter("count > 1").show()

spark.stop()