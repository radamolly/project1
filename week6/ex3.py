import pandas as pd

dates = pd.Series(['2023-01-01 07:30:22', '2023-01-02 07:30:22', '2023-01-03 07:30:22'])
dt_series = pd.to_datetime(dates)
print(dt_series.dt.year)
print(dt_series.dt.month)
print(dt_series.dt.day_name())

