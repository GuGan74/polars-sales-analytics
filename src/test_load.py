from load_data import load_sales_data
from cleaning import clean_sales_data
from analysis import monthly_sales, sales_by_region, sales_by_category

df = load_sales_data("data/raw/sales.csv")
cleaned_df = clean_sales_data(df)

monthly = monthly_sales(cleaned_df).collect()
region = sales_by_region(cleaned_df).collect()
category = sales_by_category(cleaned_df).collect()

print("\nMonthly Sales:")
print(monthly.head())

print("\nSales by Region:")
print(region)

print("\nSales by Category:")
print(category)

