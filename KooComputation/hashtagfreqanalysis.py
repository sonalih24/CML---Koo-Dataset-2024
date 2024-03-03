import json
import matplotlib.pyplot as plt
import re
from collections import Counter
from wordcloud import WordCloud

file_path = '/home/opc/koo-data/Posts/hi_posts.json'
with open(file_path, 'r', encoding='utf-8') as file:
    posts = json.load(file)

all_hashtags = []


# Iterate through each post entry
for post in posts:

   if 'title' in post and isinstance(post['title'], str):
        # Extract hashtags from the title using regular expressions
        hashtags = re.findall(r'#\w+', post['title'])
        # Add the extracted hashtags to the set
        all_hashtags.extend([tag.lower() for tag in hashtags])
     #    [tag for tag in hashtags if re.match(r'^#[A-Za-z0-9_]+$', tag)]

hashtag_count = {}

hashtag_count = Counter(all_hashtags)

for uniquehash, count in hashtag_count.most_common(30):
     print(f"{uniquehash}: {count}")


