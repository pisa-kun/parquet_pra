import pandas as pd
from datetime import datetime

dt = datetime.now()
df = pd.DataFrame({
    "id": [1,2,3],
    "name": ["Morino", "Arisugawa", "Saijyo"],
    "rating": [3.5, None, 4.2],
    "created_at": [dt, dt, dt],
});

print(df.info())
print(df)

### TODO: making directory "data"
df.to_csv('data/to_csv.csv', index=False)
df.to_csv('data/to_csv_nheader.csv', header=False)