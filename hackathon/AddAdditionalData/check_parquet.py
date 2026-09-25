import pyarrow.parquet as pq

print("=== PROCESSES ===")
print(
    pq.read_table("processes.parquet")
      .to_pandas()
)

print()

print("=== EXCHANGES ===")
print(
    pq.read_table("exchanges.parquet")
      .to_pandas()
)