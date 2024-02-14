from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.master('local[*]').appName('EmpSession').getOrCreate()
# df = spark.read.csv('employees.csv',header=True,inferSchema=True)
# df.show()
# df.describe().show()
employees = spark.createDataFrame([(1, "John", "Engineering"), (2, "Mike", "HR"), (3, "Sara", "Finance")], ["emp_id", "name", "department"])
addresses = spark.createDataFrame([(1, "NY"), (2, "LA"), (4, "DC")], ["emp_id", "address"])

employees.show()
addresses.show()

result = employees.join(addresses,'emp_id',how='inner')
result.show()
result = employees.join(addresses,'emp_id',how='outer')
result.show()
result = employees.join(addresses,'emp_id',how='left_outer')
result.show()
result = employees.join(addresses,'emp_id',how='right_outer')
result.show()
result = employees.join(addresses,'emp_id',how='left_semi')
result.show()
result = employees.join(addresses,'emp_id',how='left_anti')
result.show()
employees.select(current_date().alias("current_date")).show(1)






