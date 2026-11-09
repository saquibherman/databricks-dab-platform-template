from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.profile("DEFAULT").clusterId("1029-175814-e09kgnno").getOrCreate()
spark.sql("SELECT 1").show()
