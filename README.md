# Scalable Sales Analytics using Polars (Code-Only Project)

## Overview
This project demonstrates a fully code-based, scalable sales analytics pipeline built using **Polars** with lazy execution.
The goal of this project is to show how real-world analytical workflows can be implemented efficiently without relying on
Jupyter notebooks, using clean Python scripts and reproducible execution.

The pipeline processes retail sales transaction data and produces business-ready analytical outputs such as
monthly sales trends, regional performance, and category-level revenue.

---

## Business Problem
Retail organizations rely on transactional data to understand revenue patterns, regional performance,
and product demand. Traditional eager-execution data analysis approaches can become inefficient and
memory-intensive as data size grows.

This project addresses these challenges by:
- Using lazy execution for optimized query planning
- Separating ingestion, cleaning, and analytics logic
- Generating reusable, BI-ready outputs

---

## Dataset Description
- Superstore retail sales dataset
- Each row represents a product-level transaction within a customer order
- Key dimensions:
  - Time: Order Date, Ship Date
  - Geography: Region, State, City
  - Product hierarchy: Category, Sub-Category
- Key metric:
  - Sales (revenue)

---

## Project Architecture & Workflow
1. **Data Ingestion**
   - Load raw CSV data using Polars `scan_csv` (lazy execution)
2. **Data Cleaning**
   - Normalize column names to snake_case
   - Parse date fields
   - Remove unused and non-analytical columns
3. **Analytics Layer**
   - Monthly sales trend analysis
   - Revenue aggregation by region
   - Revenue aggregation by product category
4. **Output Generation**
   - Export analytics-ready CSV files
   - Generate visualizations using Python scripts

All steps are executed through script-based pipelines without notebooks.

---

## Tech Stack
- Python 3
- Polars (Lazy Execution, Expressions)
- Matplotlib (for visualizations)
- CSV outputs (BI / dashboard ready)

---

## Project Structure
polars-sales-analytics/
├── data/
│ └── raw/
│ └── sales.csv
├── src/
│ ├── load_data.py
│ ├── cleaning.py
│ ├── analysis.py
│ ├── visualize.py
│ └── main.py
├── outputs/
│ ├── monthly_sales.csv
│ ├── sales_by_region.csv
│ ├── sales_by_category.csv
│ └── plots/
│ ├── monthly_sales.png
│ ├── sales_by_region.png
│ └── sales_by_category.png
├── README.md
├── requirements.txt
└── .gitignore

---

## Key Analytics Performed
- Monthly revenue trend analysis
- Sales distribution by region
- Sales distribution by product category
- Schema normalization and date parsing using Polars expressions

---

## How to Run (Code-Only)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py
python src/visualize.py
