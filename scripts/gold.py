from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("Gold Layer").getOrCreate()

input_path = "/opt/airflow/project/output/silver_orders"
output_path = "/opt/airflow/project/output/gold_product_sales"

df = spark.read.parquet(input_path)

gold_df = df.groupBy("product_name").agg(
    sum("total_sales").alias("revenue")
)

gold_df.write.mode("overwrite").parquet(output_path)

spark.stop()    