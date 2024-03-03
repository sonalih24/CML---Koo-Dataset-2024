import os

# Path to the hi_comments.json file
file_path = '/home/opc/koo-data/Comments/hi_comments.json'

# Counter for comments
comment_count = 0

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the file in chunks of 1024 bytes
        while True:
            chunk = file.read(1024)
            if not chunk:  # End of file
                break
            comment_count += chunk.count('{')  # Count occurrences of {

    print(f"hi_comments.json contains approximately {comment_count} comments.")
except Exception as e:
    print(f"An error occurred: {e}")

