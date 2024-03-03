import json
from datetime import datetime
import matplotlib.pyplot as plt

# Load JSON data for English posts
with open('/home/opc/koo-data/Posts/en_posts.json', 'r') as file:
    en_data = json.load(file)

# Load JSON data for Hindi posts
with open('/home/opc/koo-data/Posts/hi_posts.json', 'r') as file:
    hi_data = json.load(file)

# Extract creation timestamps for English posts and convert to datetime objects
en_timestamps = [datetime.utcfromtimestamp(entry['createdAt']) for entry in en_data]

# Extract creation timestamps for Hindi posts and convert to datetime objects
hi_timestamps = [datetime.utcfromtimestamp(entry['createdAt']) for entry in hi_data]

# Combine timestamps from both languages
timestamps = en_timestamps + hi_timestamps

# Filter timestamps before April 2020
timestamps = [timestamp for timestamp in timestamps if timestamp >= datetime(2020, 4, 1)]

# Group timestamps by two-month period
post_activity = {}
for timestamp in timestamps:
    year_month = (timestamp.year, timestamp.month - (timestamp.month % 2))  # Grouping by every two months
    if year_month in post_activity:
        post_activity[year_month] += 1
    else:
        post_activity[year_month] = 1

# Sort the data by year and month
sorted_post_activity = dict(sorted(post_activity.items()))

# Filter out months with zero activity
sorted_post_activity = {k: v for k, v in sorted_post_activity.items() if v != 0}

# Print number of posts per two months/year for both languages
for year_month, count in sorted_post_activity.items():
    print(f"{year_month[0]}-{year_month[1]:02}: {count} post(s) per two months")

# Extract years and months for labeling
years_months = list(sorted_post_activity.keys())
counts = list(sorted_post_activity.values())

# Plot the data as a line chart
plt.figure(figsize=(12, 6))
plt.plot(range(len(years_months)), counts, marker='o', linestyle='-', label='Combined')
plt.title('Post Activity Over Time (Bimonthly)')
plt.xlabel('Year-Month')
plt.ylabel('Number of Posts')
plt.xticks(range(len(years_months)), [f'{year}-{month:02}' for year, month in years_months], rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)

# Save and show the plot
plt.tight_layout()
plt.savefig('/home/opc/koo-data/! Results & Graphs/combined_analy.png')
plt.show()
