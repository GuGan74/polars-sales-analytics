import polars as pl

def monthly_sales(df: pl.LazyFrame) -> pl.LazyFrame:
    """
    Calculate total sales per month.
    """
    return (
        df.with_columns(
            pl.col("order_date").dt.strftime("%Y-%m").alias("year_month")
        )
        .group_by("year_month")
        .agg(pl.sum("sales").alias("total_sales"))
        .sort("year_month")
    )


def sales_by_region(df: pl.LazyFrame) -> pl.LazyFrame:
    """
    Calculate total sales by region.
    """
    return (
        df.group_by("region")
        .agg(pl.sum("sales").alias("total_sales"))
        .sort("total_sales", descending=True)
    )


def sales_by_category(df: pl.LazyFrame) -> pl.LazyFrame:
    """
    Calculate total sales by category.
    """
    return (
        df.group_by("category")
        .agg(pl.sum("sales").alias("total_sales"))
        .sort("total_sales", descending=True)
    )
