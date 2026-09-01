import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv('Mall_Customers.csv')

# 2. Rule-Based Data Analytics (Bypassing the blocked ML library)
def assign_group(row):
    income = row['Annual Income (k$)']
    spend = row['Spending Score (1-100)']
    
    if income >= 70 and spend >= 70:
        return 'Target (High Income, High Spend)'
    elif income >= 70 and spend <= 30:
        return 'Careful (High Income, Low Spend)'
    elif income <= 40 and spend >= 70:
        return 'Careless (Low Income, High Spend)'
    elif income <= 40 and spend <= 30:
        return 'Sensible (Low Income, Low Spend)'
    else:
        return 'Standard (Mid Income, Mid Spend)'

# Apply the logic to group the customers
df['Customer_Group'] = df.apply(assign_group, axis=1)

# 3. Create and save the visualization
plt.style.use('dark_background')
plt.figure(figsize=(10, 6))

# Define colors for each group
colors = {
    'Target (High Income, High Spend)': '#ff9999', 
    'Standard (Mid Income, Mid Spend)': '#66b3ff', 
    'Careful (High Income, Low Spend)': '#99ff99', 
    'Careless (Low Income, High Spend)': '#ffcc99', 
    'Sensible (Low Income, Low Spend)': '#c2c2f0'
}

# Plot the data
for group, color in colors.items():
    subset = df[df['Customer_Group'] == group]
    plt.scatter(subset['Annual Income (k$)'], subset['Spending Score (1-100)'], 
                s=50, c=color, label=group)

plt.title('Customer Market Segmentation (Rule-Based Analytics)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig('customer_groups.png')

print("Success! The data analytics model ran and saved 'customer_groups.png'.")