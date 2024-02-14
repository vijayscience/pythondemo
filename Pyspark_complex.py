from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.master('local[*]').appName('Spark1').getOrCreate()

brandsDf = spark.createDataFrame([(2018, 'Apple', 45000),
                                  (2019, 'Apple', 35000),
                                  (2020, 'Apple', 75000),
                                  (2018, 'Samsung', 15000),
                                  (2019, 'Samsung', 20000),
                                  (2020, 'Samsung', 25000),
                                  (2018, 'Nokia', 21000),
                                  (2019, 'Nokia', 17000),
                                  (2020, 'Nokia', 14000)], ['Year', 'Brand', 'Amount'])

# brandsDf.show()

Windowspec = Window.partitionBy('Brand').orderBy('Year')
profitLossdf = brandsDf.withColumn('PrevYearAmount', lag('Amount', 1, 0).over(Windowspec))
#Find out whether its a profit or loss, Profit 1 ,loss 0.
# profitLossdf.show()
profitLossdf = profitLossdf.withColumn('profLoss',when((profitLossdf.Amount - profitLossdf.PrevYearAmount)<=0,0).otherwise(1))
profitLossdf.show()

# profitLossdf.crosstab('Brand','profLoss').show()
companystatus= profitLossdf.crosstab('Brand','profLoss').withColumnRenamed('0','YearsLoss').withColumnRenamed('1','YearsProfit').withColumnRenamed('Brand_profLoss','Brand')
companystatus.show()

# finally filter the Brands no years of loss

companystatus.filter('YearsLoss==0').select('Brand').show()
