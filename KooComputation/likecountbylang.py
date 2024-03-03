import os
import ijson
import matplotlib.pyplot as plt

likes_directory = '/home/opc/koo-data/Likes'

likes_per_language = {}
total_likes = 0  

def process_file(file_path, language_code):
    global total_likes
    if language_code == 'en-NG':
        language_code = 'en'
    try:
        with open(file_path, 'rb') as file:  
            likes_count = sum(1 for _ in ijson.items(file, 'item'))
            likes_per_language[language_code] = likes_per_language.get(language_code, 0) + likes_count
            total_likes += likes_count 
    except Exception as e: 
        print(f"An error occurred while processing file: {file_path}")
        print(f"Error message: {e}")

for filename in os.listdir(likes_directory):
    if filename.endswith('.json'):
        language_code = filename.split('_')[0]
        file_path = os.path.join(likes_directory, filename)
        process_file(file_path, language_code)

top_languages = sorted(likes_per_language, key=likes_per_language.get, reverse=True)[:10]
top_counts = [likes_per_language[language] for language in top_languages]

plt.figure(figsize=(10, 8)) 
bars = plt.bar(top_languages, top_counts, color='skyblue')
plt.xlabel('Language Code')
plt.ylabel('Number of Likes')
plt.title('Top 10 Languages by Number of Likes')

for bar in bars:
    height = bar.get_height()
    annotation = f'{height/1e6:.1f}M' 
    y_offset = 0.03 * height  
    plt.text(bar.get_x() + bar.get_width() / 2.0, height + y_offset, annotation, ha='center', va='bottom')

plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x/1e6:.1f}M'))

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/home/opc/koo-data/! Results & Graphs/top_likes_per_language.png')
plt.close()

print(f"Total number of likes across all languages: {total_likes}")

for language, count in zip(top_languages, top_counts):
    print(f"Language: {language}, Likes count: {count}")





