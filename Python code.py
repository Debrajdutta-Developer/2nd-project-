# ==============================
# 📊 SALES PERFORMANCE ANALYSIS
# ==============================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# STEP 1: Load Dataset
# ------------------------------
# Upload your CSV file in Colab and replace filename
df = pd.read_csv('your_dataset.csv')

# Preview data
print("First 5 rows:")
print(df.head())

# ------------------------------
# STEP 2: Data Cleaning
# ------------------------------

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove missing values
df.dropna(inplace=True)

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# ------------------------------
# STEP 3: KPIs
# ------------------------------

# Total Revenue
total_revenue = df['Sales'].sum()

# Total Profit
total_profit = df['Profit'].sum()

# Average Order Value
total_orders = df['Order ID'].nunique()
aov = total_revenue / total_orders

print("\n📊 KPIs:")
print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Average Order Value:", aov)

# ------------------------------
# STEP 4: Analysis
# ------------------------------

# Sales by Region
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

# Sales by Product
product_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)

print("\nTop Regions:")
print(region_sales)

print("\nTop Products:")
print(product_sales)

# ------------------------------
# STEP 5: Visualization
# ------------------------------

# Bar Chart: Sales by Region
plt.figure()
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# Line Chart: Sales Over Time
sales_over_time = df.groupby('Order Date')['Sales'].sum()

plt.figure()
sales_over_time.plot()
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()

# ------------------------------
# STEP 6: Additional Insights
# ------------------------------

# Lowest performing region
lowest_region = region_sales.idxmin()

# Highest performing product
top_product = product_sales.idxmax()

print("\n📌 Insights:")
print(f"Top Region: {region_sales.idxmax()}")
print(f"Lowest Region: {lowest_region}")
print(f"Top Product: {top_product}")
