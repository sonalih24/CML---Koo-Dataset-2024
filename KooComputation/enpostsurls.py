import os
import json
from urllib.parse import urlparse
from collections import Counter
import matplotlib.pyplot as plt

posts_directory = '/home/opc/koo-data/Posts'
en_posts_file = os.path.join(posts_directory, 'en_posts.json')
en_ng_posts_file = os.path.join(posts_directory, 'en-NG_posts.json')

domain_mapping = {
    'youtu.be': 'youtube.com',
    'www.youtube.com': 'youtube.com',
    'instagram.com': 'instagram.com',
    'www.instagram.com': 'instagram.com',
    'facebook.com': 'facebook.com',
    'www.facebook.com': 'facebook.com',
    'twitter.com': 'twitter.com',
    'www.twitter.com': 'twitter.com',
    't.co': 'twitter.com',
    't.me': 'twitter.com',
    'fb.watch': 'facebook.com',
    'twitch.tv': 'twitch.tv',
    'www.twitch.tv': 'twitch.tv',
    'play.google.com': 'google.com',
}

def normalize_url(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.lower()
        domain = domain_mapping.get(domain, domain).replace('www.', '')
        return domain
    except ValueError:
        return None

def extract_urls(post_title):
    urls = []
    words = post_title.split()
    for word in words:
        if word.startswith('http://') or word.startswith('https://'):
            normalized_url = normalize_url(word)
            if normalized_url and not 'bit.ly' in normalized_url:
                urls.append(normalized_url)
    return urls

urls_counter = Counter()

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            posts_data = json.load(file)
            for post in posts_data:
                title = post.get('title', '')
                if title:
                    urls = extract_urls(title)
                    urls_counter.update(urls)
    except json.decoder.JSONDecodeError as e:
        print(f"Error reading the JSON file: {file_path}")
        print(f"Error message: {e}")

process_file(en_posts_file)
process_file(en_ng_posts_file)

top_10_urls = urls_counter.most_common(10)

labels = [url for url, _ in top_10_urls]
counts = [count for _, count in top_10_urls]

plt.figure(figsize=(10, 8))
bars = plt.barh(labels, counts, color='skyblue')

for bar in bars:
    label = f'{bar.get_width()/1e6:.1f}M' if bar.get_width() >= 1e6 else f'{bar.get_width()/1e3:.1f}K'
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, label, va='center', ha='left')

plt.xlabel('Frequency')
plt.title('Top 10 URLs in English Posts')
plt.gca().invert_yaxis()

xticks = plt.gca().get_xticks()
new_labels = [f'{x/1e6:.1f}M' if x >= 1e6 else f'{x/1e3:.1f}K' for x in xticks]
plt.gca().set_xticklabels(new_labels)

plt.tight_layout()

output_file_path = '/home/opc/koo-data/! Results & Graphs/top_en_urls.png'
plt.savefig(output_file_path)
plt.close()

print(output_file_path)
