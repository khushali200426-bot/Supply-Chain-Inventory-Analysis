import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("supply_chain_inventory_analysis.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

print(df.isnull().sum())

# Fill missing Supplier values with the most frequent supplier
df["Supplier"] = df["Supplier"].fillna(df["Supplier"].mode()[0])

# Fill missing Lead Time with median
df["Lead_Time_Days"] = df["Lead_Time_Days"].fillna(df["Lead_Time_Days"].median())

# Fill missing Defect Rate with median
df["Defect_Rate"] = df["Defect_Rate"].fillna(df["Defect_Rate"].median())


df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

print(df.isnull().sum())
print(df.shape)

# EDA - Supply Chain Analysis

# Total Orders
print("Total Orders:", df["Order_ID"].nunique())

# Total Units Ordered
print("Total Units Ordered:", df["Units_Ordered"].sum())

# Total Units Sold
print("Total Units Sold:", df["Units_Sold"].sum())

# Total Stock Level
print("Total Stock Level:", df["Stock_Level"].sum())

# Average Defect Rate
print("Average Defect Rate:", df["Defect_Rate"].mean())

# Average Lead Time
print("Average Lead Time:", df["Lead_Time_Days"].mean()) 

# Supplier Analysis 
# Orders by Supplier
supplier_orders = df.groupby("Supplier")["Order_ID"].nunique().sort_values(ascending=False)

print("Orders by Supplier:")
print(supplier_orders)

# Units Ordered by Supplier
supplier_units = df.groupby("Supplier")["Units_Ordered"].sum().sort_values(ascending=False)

print("\nUnits Ordered by Supplier:")
print(supplier_units)

# Average Defect Rate by Supplier
supplier_defect = df.groupby("Supplier")["Defect_Rate"].mean().sort_values(ascending=False)

print("\nAverage Defect Rate by Supplier:")
print(supplier_defect)

# Inventory Analysis

# Total inventory stock
print("Total Stock:", df["Stock_Level"].sum())

# Average stock level
print("Average Stock Level:", df["Stock_Level"].mean())

# Products with low stock
low_stock = df[df["Stock_Level"] < df["Reorder_Level"]]

print("\nLow Stock Records:")
print(low_stock[["Product", "Stock_Level", "Reorder_Level"]])

# Count of low-stock records
print("\nLow Stock Records Count:", len(low_stock))

# Inventory by Product Category
category_stock = df.groupby("Product_Category")["Stock_Level"].sum().sort_values(ascending=False)

print("\nStock by Product Category:")
print(category_stock)

# Product Performance Analysis

# Total units sold by product
product_sales = (
    df.groupby("Product")["Units_Sold"]
    .sum()
    .sort_values(ascending=False)
)

print("\nUnits Sold by Product:")
print(product_sales)

# Total units ordered by product
product_orders = (
    df.groupby("Product")["Units_Ordered"]
    .sum()
    .sort_values(ascending=False)
)

print("\nUnits Ordered by Product:")
print(product_orders)

# Top 10 products by units sold
top_products = product_sales.head(10)

print("\nTop 10 Products by Units Sold:")
print(top_products)

# Sales fulfillment rate
df["Fulfillment_Rate"] = (
    df["Units_Sold"] / df["Units_Ordered"]
) * 100

print("\nAverage Fulfillment Rate:",
      round(df["Fulfillment_Rate"].mean(), 2), "%")

# Revenue & Profit Analysis

# Revenue
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

# Total Cost
df["Total_Cost"] = df["Units_Sold"] * df["Unit_Cost"]

# Profit
df["Profit"] = df["Revenue"] - df["Total_Cost"]

# Profit Margin
df["Profit_Margin"] = (df["Profit"] / df["Revenue"]) * 100

print("\nTotal Revenue:", round(df["Revenue"].sum(), 2))
print("Total Cost:", round(df["Total_Cost"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Average Profit Margin:", round(df["Profit_Margin"].mean(), 2), "%")

# Profit by Product Category
category_profit = (
    df.groupby("Product_Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\nProfit by Product Category:")
print(category_profit)

# Top 10 profitable products
top_profit_products = (
    df.groupby("Product")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Profitable Products:")
print(top_profit_products)


# Top 10 loss-making products
loss_products = (
    df.groupby("Product")["Profit"]
    .sum()
    .sort_values(ascending=True)
    .head(10)
)

print("\nTop 10 Loss-Making Products:")
print(loss_products)


print(df.columns)


# Sales by Product Category
sales_by_category = (
    df.groupby("Product_Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Product Category:")
print(sales_by_category)



# Profit by Product Category
profit_by_category = (
    df.groupby("Product_Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\nProfit by Product Category:")
print(profit_by_category)


# Sales by Region
sales_by_region = (
    df.groupby("Region")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Region:")
print(sales_by_region)


# Profit by Region
profit_by_region = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\nProfit by Region:")
print(profit_by_region)


# Monthly Sales Trend
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Revenue"]
    .sum()
)

print("\nMonthly Sales:")
print(monthly_sales)


# Monthly Profit Trend
monthly_profit = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Profit"]
    .sum()
)

print("\nMonthly Profit:")
print(monthly_profit)

# Top Suppliers by Revenue
top_suppliers = (
    df.groupby("Supplier")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Suppliers by Revenue:")
print(top_suppliers)


# Top Suppliers by Profit
top_profit_suppliers = (
    df.groupby("Supplier")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Suppliers by Profit:")
print(top_profit_suppliers)


# Top 10 Products by Stock Level
top_stock_products = (
    df.groupby("Product")["Stock_Level"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Stock Level:")
print(top_stock_products)



# Low Stock Products
low_stock = df[df["Stock_Level"] < df["Reorder_Level"]]

print("\nLow Stock Products:")
print(low_stock[["Product", "Stock_Level", "Reorder_Level"]].head(10))


# Delivery Status Analysis
delivery_status = (
    df["Delivery_Status"]
    .value_counts()
)

print("\nDelivery Status:")
print(delivery_status)

# Average Defect Rate
avg_defect_rate = df["Defect_Rate"].mean()

print("\nAverage Defect Rate:")
print(avg_defect_rate)

# Average Fulfillment Rate
avg_fulfillment_rate = df["Fulfillment_Rate"].mean()

print("\nAverage Fulfillment Rate:")
print(avg_fulfillment_rate)


# Average Lead Time
avg_lead_time = df["Lead_Time_Days"].mean()

print("\nAverage Lead Time:")
print(avg_lead_time)




# Top 10 Profitable Products - Visualization

top_profit_products.sort_values().plot(
    kind="barh",
    figsize=(10, 6),
    title="Top 10 Profitable Products"
)

plt.xlabel("Total Profit")
plt.ylabel("Product")
plt.tight_layout()
plt.show() 

# 2. Sales by Product Category

sales_by_category.plot(
    kind="bar",
    figsize=(8, 5),
    title="Sales by Product Category"
)

plt.xlabel("Product Category")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()


# 3. Profit by Region

profit_by_region.plot(
    kind="bar",
    figsize=(8, 5),
    title="Profit by Region"
)

plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.show()


# 4. Monthly Sales Trend

monthly_sales.plot(
    kind="line",
    figsize=(10, 5),
    marker="o",
    title="Monthly Sales Trend"
)

plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# 5. Delivery Status

delivery_status.plot(
    kind="bar",
    figsize=(8, 5),
    title="Delivery Status"
)

plt.xlabel("Delivery Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()



# 6. Low Stock Products

low_stock_counts = (
    low_stock["Product"]
    .value_counts()
    .head(10)
)

low_stock_counts.sort_values().plot(
    kind="barh",
    figsize=(10, 6),
    title="Top 10 Low Stock Products"
)

plt.xlabel("Number of Low Stock Records")
plt.ylabel("Product")
plt.tight_layout()
plt.show()


# Final Business Insights

print("\n========== FINAL BUSINESS INSIGHTS ==========")

print("Most Profitable Product:", top_profit_products.idxmax())
print("Best Product Category:", sales_by_category.idxmax())
print("Most Profitable Region:", profit_by_region.idxmax())
print("Best Supplier:", top_profit_suppliers.idxmax())
print("Most Common Delivery Status:", delivery_status.idxmax())
print("Low Stock Records:", len(low_stock))