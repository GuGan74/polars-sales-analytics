import polars as pl

def clean_sales_data(df: pl.LazyFrame) -> pl.LazyFrame:
    """
    Clean and prepare sales data for analysis.
    """

    # Rename columns to snake_case
    df = df.rename({
        "Order ID": "order_id",
        "Order Date": "order_date",
        "Ship Date": "ship_date",
        "Ship Mode": "ship_mode",
        "Customer ID": "customer_id",
        "Segment": "segment",
        "City": "city",
        "State": "state",
        "Region": "region",
        "Category": "category",
        "Sub-Category": "sub_category",
        "Product Name": "product_name",
        "Sales": "sales",
    })

    # Parse dates (DD/MM/YYYY)
    df = df.with_columns([
        pl.col("order_date").str.strptime(pl.Date, "%d/%m/%Y"),
        pl.col("ship_date").str.strptime(pl.Date, "%d/%m/%Y"),
    ])

    # Drop unused columns
    df = df.drop([
        "Row ID",
        "Country",
        "Postal Code",
        "Customer Name",
        "Product ID",
    ])

    return df
