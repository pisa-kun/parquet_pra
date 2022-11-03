import pandas as pd

loaded_df = pd.read_parquet("data/data.parquet")

print(loaded_df.info())
print(loaded_df)