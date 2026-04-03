from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Silver Layer").getOrCreate()

input_path = "/opt/airflow/project/output/bronze_orders"
output_path = "/opt/airflow/project/output/silver_orders"

df = spark.read.parquet(input_path)

silver_df = df.withColumn(
    "total_sales",
    col("price") * col("quantity")
)

silver_df.write.mode("overwrite").parquet(output_path)

spark.stop()