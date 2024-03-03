import os
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

comments_directory = '/home/opc/koo-data/Comments'

comments_per_language = {}
total_comments = 0  

hi_comments_count = 20438609
comments_per_language['hi'] = hi_comments_count
total_comments += hi_comments_count  

for filename in os.listdir(comments_directory):
    if filename.endswith('.json'):
        language_code = filename.split('_')[0]

        if language_code == 'en-NG':
            language_code = 'en'
        
        if language_code == 'hi':
            print("Skipping 'hi' comments file as it's already manually added.")
            continue
        
        file_path = os.path.join(comments_directory, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                comments_data = json.load(file)
                comments_count = len(comments_data)
                comments_per_language[language_code] = comments_per_language.get(language_code, 0) + comments_count
                total_comments += comments_count  
        except json.decoder.JSONDecodeError as e:
            print(f"An error occurred while processing file: {filename}")
            print(f"Error message: {e}")
            continue

sorted_languages = sorted(comments_per_language, key=comments_per_language.get, reverse=True)[:10]
sorted_counts = [comments_per_language[language] for language in sorted_languages]

plt.figure(figsize=(10, 6))
bars = plt.bar(sorted_languages, [count / 1e6 for count in sorted_counts], color='skyblue')
plt.xlabel('Language Code')
plt.ylabel('Number of Comments (in millions)')
plt.title('Top 10 Languages by Number of Comments')

plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:.1f}M'))

for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{height:.1f}M',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), 
                 textcoords="offset points",
                 ha='center', va='bottom')

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/home/opc/koo-data/! Results & Graphs/top_comments_by_language.png')
plt.close()

print(f"Total number of comments across all languages: {total_comments}")

for language in sorted_languages:
    print(f"Language: {language}, Comment count: {comments_per_language[language]}")









