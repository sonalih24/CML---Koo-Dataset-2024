import json
from datetime import datetime
import matplotlib.pyplot as plt

# Function to format numbers with abbreviated units
def format_number(number):
    if number >= 1e6:
        return '{:.1f}M'.format(number / 1e6)
    elif number >= 1e3:
        return '{:.1f}k'.format(number / 1e3)
    else:
        return str(number)

# Load JSON data from file
with open('/home/opc/koo-data/Users/koo_users.json', 'r') as file:
    data = json.load(file)

# Extract createdAt timestamps and filter dates between March 2020 and October 2023
timestamps = [entry['createdAt'] for entry in data]
dates = [datetime.fromtimestamp(timestamp) for timestamp in timestamps if datetime.fromtimestamp(timestamp) >= datetime(2020, 4, 1) and datetime.fromtimestamp(timestamp) <= datetime(2023, 4, 30)]

# Count user creations per two-month period
user_creations = {}
for date in dates:
    year_month = (date.year, date.month - (date.month % 2))  # Grouping by every two months
    if year_month in user_creations:
        user_creations[year_month] += 1
    else:
        user_creations[year_month] = 1

# Sort the data by year and month
sorted_user_creations = dict(sorted(user_creations.items()))

# console debug
for year_month, count in sorted_user_creations.items():
    print(f"{year_month[0]}-{year_month[1]:02}: {count} user(s)")
    
# Unpack sorted data into separate lists for plotting
years_months = list(sorted_user_creations.keys())
counts = list(sorted_user_creations.values())

# Extract years and months for labeling
years = [year for year, _ in years_months]
months = [month for _, month in years_months]

# Plot the data
plt.figure(figsize=(12, 6))
bars = plt.bar(range(len(years_months)), counts, color='skyblue')
plt.title('User Account Creations Over Time')
plt.xlabel('Year-Month')
plt.ylabel('Number of Account Creations')
plt.xticks(range(len(years_months)), [f'{year}-{month:02}' for year, month in years_months], rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add annotations
for bar, count in zip(bars, counts):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), format_number(count), ha='center', va='bottom')

plt.tight_layout()
plt.savefig('/home/opc/koo-data/! Results & Graphs/ha2.png')
plt.show()
