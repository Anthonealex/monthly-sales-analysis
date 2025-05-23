import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset (update path if needed)
df = pd.read_csv('Superstore.csv')

# Step 2: Convert 'Order Date' column to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Step 3: Extract Year and Month
df['YearMonth'] = df['Order Date'].dt.to_period('M')

# Step 4: Group by YearMonth and sum Sales
monthly_sales = df.groupby('YearMonth')['Sales'].sum().reset_index()

# Step 5: Convert YearMonth to string for plotting
monthly_sales['YearMonth'] = monthly_sales['YearMonth'].astype(str)

# Step 6: Plot the monthly sales trend
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales['YearMonth'], monthly_sales['Sales'], marker='o', linestyle='-')
plt.xticks(rotation=45)
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.savefig('monthly_sales_chart.png')  # Optional: Save the chart
plt.show()
