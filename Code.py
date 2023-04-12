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



import pandas as pd
import matplotlib.pyplot as plt
# Read data from CSV file
data = pd.read_csv('germination_speed.csv')
# Calculate speed of germination
data['Speed of Germination'] = data['Num Germinated'].diff()
data.loc[0, 'Speed of Germination'] = data.loc[0, 'Num Germinated'] # Fix for warning
# Visualize the results
fig, ax = plt.subplots()
ax.set_xlabel('Day')
ax.set_ylabel('Number of Seeds Germinated')
ax.plot(data['Day'], data['Num Germinated'], label='Number of Seeds Germinated')
ax2 = ax.twinx()
ax2.set_ylabel('Speed of Germination')
ax2.plot(data['Day'], data['Speed of Germination'], color='red', label='Speed of Germination')
plt.title('Germination Analysis')
plt.legend([ax.get_lines()[0], ax2.get_lines()[0]], ['Number of Seeds Germinated', 'Speed of Germination'])
plt.show()
