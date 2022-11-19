from pyspark import SparkContext
from pyspark.sql import SparkSession

spark_context = SparkContext()
spark = SparkSession(spark_context)

df = spark.read.parquet("data/H_2021.parquet")
df.show()
print("---------")
df2 = spark.read.csv("data/to_csv.csv")
df2.show()

# path = "/parquet/out/pyspark.parquet"
# df2.write.parquet("/parquet/out/pyspark.parquet").option('mode', 'FAILFAST')

# df3 = spark.read.parquet(path)
# df3.show()