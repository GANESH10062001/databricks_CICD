import dlt

@dlt.table
def silver():
  df = spark.read.table("databricks_ganesh.silver.customer_enr")
  return df