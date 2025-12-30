import polars as pl

def load_sales_data(path: str) -> pl.LazyFrame:
    """
    Load sales data using Polars lazy execution.
    """
    return pl.scan_csv(
        path,
        try_parse_dates=False,
        infer_schema_length=1000
    )

