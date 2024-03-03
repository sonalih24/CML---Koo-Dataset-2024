import os
import json
from urllib.parse import urlparse
from collections import Counter
import matplotlib.pyplot as plt

posts_directory = '/home/opc/koo-data/Posts'
hi_posts_file = os.path.join(posts_directory, 'hi_posts.json')

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
    'fb.watch': 'facebook.com',  
    'twitch.tv': 'twitch.tv',
    'www.twitch.tv': 'twitch.tv',
    'docs.google.com': 'google.com',
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

try:
    with open(hi_posts_file, 'r', encoding='utf-8') as file:
        posts_data = json.load(file)
        for post in posts_data:
            title = post.get('title', '')
            if title:
                urls = extract_urls(title)
                urls_counter.update(urls)
except json.decoder.JSONDecodeError as e:
    print(f"Error reading the JSON file: {e}")

top_10_urls = urls_counter.most_common(10)

labels = [url for url, _ in top_10_urls]
counts = [count for _, count in top_10_urls]

plt.figure(figsize=(10, 8))
bars = plt.barh(labels, counts, color='skyblue')

def format_count(count):
    if count >= 1e6:
        return f'{count/1e6:.1f}M'
    elif count >= 1e3:
        return f'{count/1e3:.1f}K'
    else:
        return str(count)

for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2,
             format_count(bar.get_width()), va='center', ha='left')

plt.xlabel('Frequency')
plt.title('Top 10 URLs in Hindi Posts')
plt.gca().invert_yaxis()

xticks = plt.gca().get_xticks()
plt.gca().set_xticklabels([format_count(x) for x in xticks])

plt.tight_layout()

bar_chart_path = '/home/opc/koo-data/! Results & Graphs/top_hi_urls.png'
plt.savefig(bar_chart_path)
plt.close()

bar_chart_path








