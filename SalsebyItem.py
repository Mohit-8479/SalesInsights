import matplotlib.pyplot as plt 
import pandas as pd 
df = pd.read_excel('SaleData.xlsx')
# print(file["Item"])

# Display the first few rows of the DataFrame to understand the data structure
print(df.head())

item_sales = df.groupby("Item")["Sale_amt"].sum().sort_values(ascending=False)
print("\nTotal Sales by Item:")
print(item_sales)

# Visualize the Total Sales by Item
plt.figure(figsize=(10, 6))
item_sales.plot(kind="bar")
plt.title("Total Sales by Item")
plt.xlabel("Item")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()





