import pandas as pd
import matplotlib.pyplot as plt
# Read data from CSV file
data = pd.read_csv('germination_data.csv')
# Calculate germination percentage
total_seeds = len(data)
healthy_seedlings = len(data[data['Germinated'] == 1])
germination_percentage = (healthy_seedlings / total_seeds) * 100
# Visualize the results
fig, ax = plt.subplots()
ax.set_xlabel('Seed Number')
ax.set_ylabel('Days to Germinate')
ax.scatter(data['Seed'], data['Germination Day'], c=data['Germinated'], cmap='coolwarm')
plt.title('Germination Analysis')
plt.text(0.5, 0.9, f'Germination Percentage: {germination_percentage:.2f}%', ha='center', va='center', transform=ax.transAxes)
plt.show()



