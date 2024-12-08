from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sha2

def anonymize_csv(input_file, output_file):
    spark = SparkSession.builder.master("local[*]").appName("CSV Anonymizer").getOrCreate()

    df = spark.read.csv(input_file, header=True, inferSchema=True)
    anonymized_df = df.withColumn("first_name", sha2(col("first_name"), 256))\
                      .withColumn("last_name", sha2(col("last_name"), 256))\
                      .withColumn("address", sha2(col("address"), 256))

    anonymized_df.write.csv(output_file, header=True, mode="overwrite")