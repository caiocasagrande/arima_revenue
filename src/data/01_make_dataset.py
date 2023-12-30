# Make dataset - from data raw to data interim

# Importing libraries
import pandas as pd

# Importing datasets
df_order_items  = pd.read_parquet('../../data/raw/olist_order_items_dataset.parquet')
df_sellers      = pd.read_parquet('../../data/raw/olist_sellers_dataset.parquet')
df_products     = pd.read_parquet('../../data/raw/olist_products_dataset.parquet')
df_orders       = pd.read_parquet('../../data/raw/olist_orders_dataset.parquet')
df_customers    = pd.read_parquet('../../data/raw/olist_customers_dataset.parquet')
df_payments     = pd.read_parquet('../../data/raw/olist_order_payments_dataset.parquet')

# Filtering df_payments
df_payments     = df_payments[df_payments['payment_sequential'] == 1]

# Merging the datasets
merged_df = (
    df_order_items
    .merge(df_orders, on='order_id', how='left')
    .merge(df_products[['product_id', 'product_category_name']], on='product_id', how='left')
    .merge(df_sellers[['seller_id', 'seller_city', 'seller_state']], on='seller_id', how='left')
    .merge(df_customers[['customer_id', 'customer_city', 'customer_state']], on='customer_id', how='left')
    .merge(df_payments[['order_id', 'payment_type', 'payment_installments', 'payment_value']], on='order_id', how='left')
)

# Organizing columns

dataset = merged_df[
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
        'order_purchase_timestamp',
        'order_approved_at',
        'shipping_limit_date',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]
]

# Saving dataset
dataset.to_parquet('../../data/interim/olist_merged_dataset.parquet')