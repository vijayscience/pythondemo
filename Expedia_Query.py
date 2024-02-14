from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window
spark = SparkSession.builder.master('local[*]').appName('Test').getOrCreate()
df = spark.read.csv('train_sample.csv',header=True,inferSchema=True,sep=',')
# df.printSchema()
# df.select("date_time").show(truncate=False)
# df.select(df['srch_destination_id'],datediff(df['srch_co'],df['srch_ci']).alias('daystay')).filter((df["srch_children_cnt"]==0) & (df["srch_adults_cnt"]==2) & (df['srch_rm_cnt']==1) & (df['is_booking']==1) & (df['cnt']>1)).sort('daystay',ascending=False).show(3)
winSpce = Window.partitionBy('srch_destination_id').orderBy(df['srch_destination_id'].asc())
df1 = df.withColumn('DenseRanks',dense_rank().over(winSpce))

df1.groupby(df1['srch_destination_id'],df1['DenseRanks']).count().sort('count',ascending=False).show()

# df1.select(df['*']).filter((df['srch_children_cnt']>0) & (df['is_booking']==0)).groupby('srch_destination_id').count().orderBy('DenseRanks',ascending=False).show()

# df.select(df['srch_destination_id'],count('*')).show()
