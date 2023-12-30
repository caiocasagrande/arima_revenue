import pandas as pd

def csv_to_parquet(csv_path, parquet_path):
    """
    Convert csv files to parquet files
    """
    df = pd.read_csv(csv_path)
    df.to_parquet(parquet_path)

    return None

files = [
    'olist_customers_dataset.',
    'olist_geolocation_dataset.',
    'olist_order_items_dataset.',
    'olist_order_payments_dataset.',
    'olist_order_reviews_dataset.',
    'olist_products_dataset.',
    'olist_sellers_dataset.',
    'product_category_name_translation.',
]

for file in files:
    
    csv_path = '../../data/raw/' + file + 'csv' 
    parquet_path = '../../data/raw/' + file + 'parquet'

    csv_to_parquet(csv_path, parquet_path)

