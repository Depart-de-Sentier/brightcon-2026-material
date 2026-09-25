import pyarrow.csv as csv
import pyarrow.parquet as pq

# Processes
processes_table = csv.read_csv("processes.csv")
pq.write_table(processes_table, "processes.parquet")

# Exchanges
exchanges_table = csv.read_csv("exchanges.csv")
pq.write_table(exchanges_table, "exchanges.parquet")

print("Parquet files created successfully.")