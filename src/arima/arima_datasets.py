# Creating ARIMA datasets

# Importing libraries
import pandas as pd

# Importing datasets
dataset = pd.read_parquet('../../data/interim/olist_preprocessed_dataset.parquet')

# Filtering dataset
dataset = dataset.loc[dataset['approved_at'] <= '2018-08-15']

# Orders dataset
arima_orders_dataset = dataset[['order_id', 'date']]
arima_orders_dataset = arima_orders_dataset.groupby(['date']).count().reset_index()

# Prices dataset
arima_prices_dataset = dataset[['price', 'date']]
arima_prices_dataset = arima_prices_dataset.groupby(['date']).sum().reset_index()

# Saving datasets
arima_orders_dataset.to_csv('../../data/interim/arima_orders_dataset.csv', index=False)
arima_prices_dataset.to_csv('../../data/interim/arima_prices_dataset.csv', index=False)