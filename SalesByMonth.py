import matplotlib.pyplot as plt 
import pandas as pd 
df = pd.read_excel('SaleData.xlsx')
# print(file["Item"])

# Display the first few rows of the DataFrame to understand the data structure
print(df.head())

# Convert OrderDate to datetime format
df['OrderDate'] = pd.to_datetime(df['OrderDate'], format='%m-%d-%y')

# Extract the month from the OrderDate and create a new column 'Month'
df['Month'] = df['OrderDate'].dt.to_period('M')

# Group by Month and calculate total sales for each month
monthly_sales = df.groupby('Month')['Sale_amt'].sum()

# Convert the 'Month' index to strings
monthly_sales.index = monthly_sales.index.strftime('%Y-%m')

print("Total Sales by Month")
print(monthly_sales.index)
print(monthly_sales.values)
# Visualize the Monthly Sales Trend
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', linestyle='-')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
