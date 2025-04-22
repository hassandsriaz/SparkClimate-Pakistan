import sys
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import last, col, when, sum

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: spark-etl [input-folder] [output-folder]")
        sys.exit(0)

    spark = SparkSession \
        .builder \
        .appName("SparkETL") \
        .getOrCreate()

    # Read the input CSV file
    weatherData = spark.read.option("inferSchema", "true").option("header", "true").csv(sys.argv[1])

    # Define a window specification
    window_spec = Window.orderBy("DATE").rowsBetween(Window.unboundedPreceding, Window.currentRow)

    # Apply transformations with window functions
    updatedWeatherData = weatherData \
        .withColumn("PRCP", last("PRCP", True).over(window_spec)) \
        .withColumn("TMAX", last("TMAX", True).over(window_spec)) \
        .withColumn("TMIN", last("TMIN", True).over(window_spec)) \
        .withColumn("TAVG", last("TAVG", True).over(window_spec))

    # Drop unnecessary columns
    updatedWeatherData = updatedWeatherData.drop("PRCP_ATTRIBUTES", "SNWD", "SNWD_ATTRIBUTES", "TMAX_ATTRIBUTES", "TAVG_ATTRIBUTES", "TMIN_ATTRIBUTES")
    
    # Count null values for each column
    null_count = updatedWeatherData.select([when(col(c).isNull(), 1).otherwise(0).alias(c) for c in updatedWeatherData.columns])
    null_count_agg = null_count.agg(*[sum(col(c)).alias(c) for c in null_count.columns])
    null_count_agg.show()

    # Display the schema and data
    updatedWeatherData.printSchema()
    updatedWeatherData.show()

    print("Total number of records: " + str(updatedWeatherData.count()))

    # Write the output to the specified folder
    updatedWeatherData.write.mode("overwrite").parquet(sys.argv[2])
