##### Cleaning and preprocessing dataset

##### 1. Importing libraries
import pandas as pd
import datetime

##### 2. Importing dataset
dataset = pd.read_parquet('../../data/interim/olist_merged_dataset.parquet')

##### 3. Shortening column names
column_names_map = {
    'order_purchase_timestamp':       'purchase_ts',
    'order_approved_at':              'approved_at',
    'shipping_limit_date':            'limit_date',
    'order_delivered_carrier_date':   'delivered_carrier',
    'order_delivered_customer_date':  'delivered_customer',
    'order_estimated_delivery_date':  'estimated_delivery'}

dataset.rename(columns=column_names_map, inplace=True)

##### 4. Changing data types
### 4.1. Converting features to datetime
# Columns to be converted to datetime
datetime_columns = ['purchase_ts', 'approved_at', 'limit_date', 'delivered_carrier', 'delivered_customer', 'estimated_delivery']

# Converting columns to datetime, ignoring missing values
dataset[datetime_columns] = dataset[datetime_columns].apply(pd.to_datetime, errors='coerce')
# The errors='coerce' parameter is used to replace missing values with NaT (not a time)

##### 5. Filtering dataset

# We will work with orders from February 2017 to August 2018, where data is well organized
# The total dataset is 112650 long, while the choosen subset is 111324 (98.82%)
# The information lost is not significant 

start_date  = '2017-02-01'
end_date    = '2018-08-31'

dataset     = dataset.loc[(dataset['purchase_ts'] >= start_date) & (dataset['purchase_ts'] <= end_date)]

##### 6. Creating Features

# Time between order approval and delivery
dataset['time_delta'] = dataset['delivered_customer'] - dataset['approved_at']
# Converting to a more readable format (e.g., hours and minutes)
dataset['time_delta_hours'] = dataset['time_delta'].astype('timedelta64[h]')

# Creating date related columns
dataset['date']       = dataset['purchase_ts'].dt.date
dataset['day']        = dataset['purchase_ts'].dt.day 
dataset['month']      = dataset['purchase_ts'].dt.month 
dataset['year']       = dataset['purchase_ts'].dt.year 
dataset['dayofweek']  = dataset['purchase_ts'].dt.dayofweek 

# Region mapping
# Creating dictionary for regions
region_mapping = {
    'Nordeste':     ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
    'Norte':        ['AC', 'AM', 'AP', 'PA', 'RO', 'RR', 'TO'],
    'Sudeste':      ['ES', 'MG', 'RJ', 'SP'],
    'Sul':          ['PR', 'RS', 'SC'],
    'Centro-Oeste': ['DF', 'GO', 'MS', 'MT']}

# Mapping states by region
dataset['customer_region'] = dataset['customer_state'].map({state: region for region, states in region_mapping.items() for state in states})

# Creating dictionary for days of the week
weekday_mapping = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'}

# Mapping 
dataset['name_dayofweek'] = dataset['dayofweek'].map(weekday_mapping)

##### 7. Organizing columns
dataset = dataset[
    [
        # Order info
        'order_id',
        'order_item_id',
        # Product info
        'product_id',
        'product_category_name',
        # Customer info
        'customer_id',
        'customer_city',
        'customer_state',
        'customer_region',
        # Seller info
        'seller_id',
        'seller_city',
        'seller_state',
        # Prices and payments info
        'price',
        'freight_value',
        'payment_type',
        'payment_installments',
        'payment_value',
        # Delivery info
        'order_status',
        'purchase_ts',
        'approved_at',
        'limit_date',
        'delivered_carrier',
        'delivered_customer',
        'time_delta',
        'time_delta_hours',
        'estimated_delivery',
        # Date related features
        'date',
        'day',
        'month',
        'year',
        'dayofweek',
        'name_dayofweek'
    ]
]

##### 8. Saving dataset
dataset.to_parquet('../../data/interim/olist_preprocessed_dataset.parquet')
