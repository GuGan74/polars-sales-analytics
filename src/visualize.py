import polars as pl
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = "outputs"
PLOT_DIR = "outputs/plots"

os.makedirs(PLOT_DIR, exist_ok=True)

def plot_monthly_sales():
    df = pl.read_csv(f"{OUTPUT_DIR}/monthly_sales.csv")
    plt.figure()
    plt.plot(df["year_month"], df["total_sales"])
    plt.xticks(rotation=45)
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.savefig(f"{PLOT_DIR}/monthly_sales.png")
    plt.close()

def plot_sales_by_region():
    df = pl.read_csv(f"{OUTPUT_DIR}/sales_by_region.csv")
    plt.figure()
    plt.bar(df["region"], df["total_sales"])
    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.savefig(f"{PLOT_DIR}/sales_by_region.png")
    plt.close()

def plot_sales_by_category():
    df = pl.read_csv(f"{OUTPUT_DIR}/sales_by_category.csv")
    plt.figure()
    plt.bar(df["category"], df["total_sales"])
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.savefig(f"{PLOT_DIR}/sales_by_category.png")
    plt.close()

if __name__ == "__main__":
    plot_monthly_sales()
    plot_sales_by_region()
    plot_sales_by_category()
    print("Charts generated successfully.")
