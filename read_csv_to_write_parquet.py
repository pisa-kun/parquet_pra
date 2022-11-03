import pandas as pd

df = pd.read_csv("data/to_csv.csv", index_col=None)
# Parquetで保存
df.to_parquet("data/data.parquet")