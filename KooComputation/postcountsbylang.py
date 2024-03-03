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

# Load JSON data from files for English and Hindi
english_data = []
hindi_data = []
with open('/home/opc/koo-data/Posts/en_posts.json', 'r') as file:
    english_data = json.load(file)
with open('/home/opc/koo-data/Posts/hi_posts.json', 'r') as file:
    hindi_data = json.load(file)

# Extract createdAt timestamps and filter dates between March 2020 and October 2023 for English data
english_timestamps = [entry['createdAt'] for entry in english_data]
english_dates = [datetime.fromtimestamp(timestamp) for timestamp in english_timestamps if datetime.fromtimestamp(timestamp) >= datetime(2020, 4, 1) and datetime.fromtimestamp(timestamp) <= datetime(2023, 4, 30)]

# Count user creations per two-month period for English data
english_user_creations = {}
for date in english_dates:
    year_month = (date.year, date.month - (date.month % 2))  # Grouping by every two months
    if year_month in english_user_creations:
        english_user_creations[year_month] += 1
    else:
        english_user_creations[year_month] = 1

# Sort the English data by year and month
sorted_english_user_creations = dict(sorted(english_user_creations.items()))

# Extract years and months for labeling
english_years_months = list(sorted_english_user_creations.keys())
english_counts = list(sorted_english_user_creations.values())

# Extract createdAt timestamps and filter dates between March 2020 and October 2023 for Hindi data
hindi_timestamps = [entry['createdAt'] for entry in hindi_data]
hindi_dates = [datetime.fromtimestamp(timestamp) for timestamp in hindi_timestamps if datetime.fromtimestamp(timestamp) >= datetime(2020, 4, 1) and datetime.fromtimestamp(timestamp) <= datetime(2023, 4, 30)]

# Count user creations per two-month period for Hindi data
hindi_user_creations = {}
for date in hindi_dates:
    year_month = (date.year, date.month - (date.month % 2))  # Grouping by every two months
    if year_month in hindi_user_creations:
        hindi_user_creations[year_month] += 1
    else:
        hindi_user_creations[year_month] = 1

# Sort the Hindi data by year and month
sorted_hindi_user_creations = dict(sorted(hindi_user_creations.items()))

# Extract years and months for labeling
hindi_years_months = list(sorted_hindi_user_creations.keys())
hindi_counts = list(sorted_hindi_user_creations.values())

# Print post occurrences for each language
print("English Post Occurrences per Two Months per Year:")
for year_month, count in sorted_english_user_creations.items():
    print(f"{year_month[0]}-{year_month[1]:02}: {count} post(s)")

print("\nHindi Post Occurrences per Two Months per Year:")
for year_month, count in sorted_hindi_user_creations.items():
    print(f"{year_month[0]}-{year_month[1]:02}: {count} post(s)")

# Plot the data
plt.figure(figsize=(12, 6))

# Plot English data
english_line, = plt.plot(range(len(english_years_months)), english_counts, color='skyblue', label='English')
plt.scatter(range(len(english_years_months)), english_counts, color='skyblue', zorder=2)

# Plot Hindi data
hindi_line, = plt.plot(range(len(hindi_years_months)), hindi_counts, color='orange', label='Hindi')
plt.scatter(range(len(hindi_years_months)), hindi_counts, color='orange', zorder=2)

plt.title('Post Creations Over Time')
plt.xlabel('Year-Month')
plt.ylabel('Number of Posts')
plt.xticks(range(len(english_years_months)), [f'{year}-{month:02}' for year, month in english_years_months], rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add annotations for English data (underneath the line)
for i, count in enumerate(english_counts):
    plt.text(i, count - 1, format_number(count), ha='center', va='top', color='blue', fontsize=8, weight='bold')

# Add annotations for Hindi data (on top of the line)
for i, count in enumerate(hindi_counts):
    plt.text(i, count + 1, format_number(count), ha='center', va='bottom', color='orangered', fontsize=8, weight='bold')


# Add legend
plt.legend(handles=[english_line, hindi_line])

plt.tight_layout()
plt.savefig('/home/opc/koo-data/! Results & Graphs/english_vs_hindi5.png')
plt.show()
