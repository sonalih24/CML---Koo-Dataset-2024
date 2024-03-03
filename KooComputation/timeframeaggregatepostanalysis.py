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

# List of file paths for each language file
file_paths = [
    '/home/opc/koo-data/Posts/af_posts.json',
    '/home/opc/koo-data/Posts/ar_posts.json',
    '/home/opc/koo-data/Posts/as_posts.json',
    '/home/opc/koo-data/Posts/bn_posts.json',
    '/home/opc/koo-data/Posts/ca_posts.json',
    '/home/opc/koo-data/Posts/cs_posts.json',
    '/home/opc/koo-data/Posts/cy_posts.json',
    '/home/opc/koo-data/Posts/de_posts.json',
    '/home/opc/koo-data/Posts/en_posts.json',
    '/home/opc/koo-data/Posts/en-NG_posts.json',
    '/home/opc/koo-data/Posts/es_posts.json',
    '/home/opc/koo-data/Posts/fil_posts.json',
    '/home/opc/koo-data/Posts/fr_posts.json',
    '/home/opc/koo-data/Posts/gu_posts.json',
    '/home/opc/koo-data/Posts/ha-NG_posts.json',
    '/home/opc/koo-data/Posts/he_posts.json',
    '/home/opc/koo-data/Posts/hi_posts.json',
    '/home/opc/koo-data/Posts/ht_posts.json',
    '/home/opc/koo-data/Posts/id_posts.json',
    '/home/opc/koo-data/Posts/it_posts.json',
    '/home/opc/koo-data/Posts/ja_posts.json',
    '/home/opc/koo-data/Posts/kn_posts.json',
    '/home/opc/koo-data/Posts/ko_posts.json',
    '/home/opc/koo-data/Posts/lv_posts.json',
    '/home/opc/koo-data/Posts/ml_posts.json',
    '/home/opc/koo-data/Posts/nl_posts.json',
    '/home/opc/koo-data/Posts/or_posts.json',
    '/home/opc/koo-data/Posts/pa_posts.json',
    '/home/opc/koo-data/Posts/pl_posts.json',
    '/home/opc/koo-data/Posts/pt_posts.json',
    '/home/opc/koo-data/Posts/ro_posts.json',
    '/home/opc/koo-data/Posts/ru_posts.json',
    '/home/opc/koo-data/Posts/sl_posts.json',
    '/home/opc/koo-data/Posts/sv_posts.json',
    '/home/opc/koo-data/Posts/ta_posts.json',
    '/home/opc/koo-data/Posts/te_posts.json',
    '/home/opc/koo-data/Posts/th_posts.json',
    '/home/opc/koo-data/Posts/tr_posts.json',
    '/home/opc/koo-data/Posts/uk_posts.json',
    '/home/opc/koo-data/Posts/ur_posts.json',
    '/home/opc/koo-data/Posts/vi_posts.json',

    # Add more file paths as needed
]

# Initialize an empty list to store all timestamps
all_timestamps = []

# Loop through each file path
for file_path in file_paths:
    with open(file_path, 'r') as file:
        data = json.load(file)
        # Extract timestamps and add them to the list
        all_timestamps.extend([entry['createdAt'] for entry in data])

# Convert timestamps to datetime objects and filter dates
dates = [datetime.fromtimestamp(timestamp) for timestamp in all_timestamps 
         if datetime.fromtimestamp(timestamp) >= datetime(2020, 4, 1) and datetime.fromtimestamp(timestamp) <= datetime(2023, 4, 30)]

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
    print(f"{year_month[0]}-{year_month[1]:02}: {count} post(s)")

# Unpack sorted data into separate lists for plotting
years_months = list(sorted_user_creations.keys())
counts = list(sorted_user_creations.values())

# Extract years and months for labeling
years = [year for year, _ in years_months]
months = [month for _, month in years_months]

# Plot the data
plt.figure(figsize=(12, 6))
bars = plt.bar(range(len(years_months)), counts, color='skyblue')
plt.title('Posts (Koos) Over Time')
plt.xlabel('Year-Month')
plt.ylabel('Number of Posts')
plt.xticks(range(len(years_months)), [f'{year}-{month:02}' for year, month in years_months], rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add annotations
for bar, count in zip(bars, counts):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), format_number(count), ha='center', va='bottom')

plt.tight_layout()
plt.savefig('/home/opc/koo-data/! Results & Graphs/ha2.png')
plt.show()
