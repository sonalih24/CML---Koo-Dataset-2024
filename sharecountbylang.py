import os
import json
import matplotlib.pyplot as plt
import numpy as np

shares_directory = '/home/opc/koo-data/Shares'

shares_per_language = {}
total_shares = 0  

for filename in os.listdir(shares_directory):
    if filename.endswith('.json'):
        language_code = filename.split('_')[0]

        if language_code == 'en-NG':
            language_code = 'en'

        file_path = os.path.join(shares_directory, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                shares_data = json.load(file)
                share_count = len(shares_data)
                if language_code in shares_per_language:
                    shares_per_language[language_code] += share_count
                else:
                    shares_per_language[language_code] = share_count
                total_shares += share_count 
        except json.decoder.JSONDecodeError as e:
            print(f"An error occurred while processing file: {filename}")
            print(f"Error message: {e}")
            continue

top_languages = sorted(shares_per_language, key=shares_per_language.get, reverse=True)[:10]
top_counts = [shares_per_language[language] for language in top_languages]

plt.figure(figsize=(10, 6))

counts_in_millions = np.array(top_counts) / 1e6

bars = plt.bar(top_languages, counts_in_millions, color='skyblue')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.1f}M', ha='center', va='bottom')

plt.xlabel('Language Code')
plt.ylabel('Shares (in millions)')
plt.title('Top 10 Languages by Number of Shares')
plt.xticks(rotation=45)
plt.tight_layout()

plt.gca().set_ylim(bottom=0) 
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.1f}'))

plt.savefig('/home/opc/koo-data/! Results & Graphs/top_shares_per_language.png')
plt.close()

print(f"Total share count: {total_shares}")

for language, count in zip(top_languages, top_counts):
    print(f"Language: {language}, Share count: {count}")
