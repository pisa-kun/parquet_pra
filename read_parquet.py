import pandas as pd

loaded_df = pd.read_parquet("data/H_2021.parquet")

print(loaded_df.info())
print(loaded_df)