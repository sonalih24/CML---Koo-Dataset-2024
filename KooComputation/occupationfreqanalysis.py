import json
import matplotlib.pyplot as plt
from collections import Counter

file_path = '/home/opc/koo-data/Users/koo_users.json'

with open(file_path, 'r', encoding='utf-8') as file:
    koo_users = json.load(file)

titles = []

for users in koo_users: 
    title = users.get('title', '')
    if isinstance(title, str) and title:
        titles.append(title.lower())

title_counts = Counter(titles)

total = sum(title_counts.values())

print("Occupation counts:")
for title, count in title_counts.most_common(10):
    print(f"{title}: {count}")
     
print("Total:", total)

proportiondict = {}
print("\nProportion analysis:")
for title, count in title_counts.items():
    percentage_calc = ((count / total) * 100)  # Calculate percentage based on total occurrences
    percentage_calc = round(percentage_calc, 2)
    proportiondict[title] = percentage_calc

percentdebug = sum(proportiondict.values())
print("Total percent:", percentdebug)

sorted_titles = sorted(proportiondict, key=proportiondict.get, reverse=True)
top_10_titles = sorted_titles[:10]  # Get the top 10 titles by percentage

graph_occupations = top_10_titles
graph_counts = [title_counts[title] for title in graph_occupations]
graph_percentages = [proportiondict[title] for title in graph_occupations]

plt.figure(figsize=(14, 6))
bars = plt.barh(graph_occupations, graph_counts, color='skyblue')  # Horizontal bar chart
for bar, percent in zip(bars, graph_percentages):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{percent}%', 
             ha='left', va='center')  # Adjusting annotation position
plt.xlabel('Number of Occurrences')
plt.ylabel('Occupation')
plt.title('Occupation Distribution among Top 10 Occupations // with percent among total occurences')
plt.tight_layout()
plt.savefig('/home/opc/koo-data/! Results & Graphs/occupationdistbarchart2_hz.png')
