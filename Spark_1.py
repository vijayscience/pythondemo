from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.master('local[*]').appName('Spark1').getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.csv('employees.csv', header=True, inferSchema=True, sep=',')
df.createOrReplaceTempView('employeeTemp')
df.show(5)

# df.printSchema()

# df.filter(col('SALARY') > 9000).groupby('MANAGER_ID').agg(count('DEPARTMENT_ID')).show()

# Display employees and their manager
df.alias('e1').join(df.alias('e2'), how='left_outer', on=(col('e1.MANAGER_ID') == col('e2.EMPLOYEE_ID'))).select(col('e1.FIRST_NAME'),col('e2.FIRST_NAME').alias('Manager')).show()

# Employees who work in the same department as Taylor
df.alias('e1').join(df.alias('e2'), how='left_outer',on=(col('e1.department_id') == col('e2.DEPARTMENT_ID'))).filter(
    'Taylor' == col("e1.LAST_NAME")).select("e2.FIRST_NAME" ,"e2.LAST_NAME" ,"e2.DEPARTMENT_ID").show()

# Salary difference between jobs maximum and employees


