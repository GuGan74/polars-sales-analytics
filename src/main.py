from load_data import load_sales_data
from cleaning import clean_sales_data
from analysis import (
    monthly_sales,
    sales_by_region,
    sales_by_category,
)

OUTPUT_DIR = "outputs"

def main():
    # Load data lazily
    df = load_sales_data("data/raw/sales.csv")

    # Clean data
    cleaned_df = clean_sales_data(df)

    # Analytics
    monthly_df = monthly_sales(cleaned_df).collect()
    region_df = sales_by_region(cleaned_df).collect()
    category_df = sales_by_category(cleaned_df).collect()

    # Export results
    monthly_df.write_csv(f"{OUTPUT_DIR}/monthly_sales.csv")
    region_df.write_csv(f"{OUTPUT_DIR}/sales_by_region.csv")
    category_df.write_csv(f"{OUTPUT_DIR}/sales_by_category.csv")

    print("Analytics pipeline completed successfully.")


if __name__ == "__main__":
    main()
