import os
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

users_file_path = '/home/opc/koo-data/Users/koo_users.json'

if os.path.exists(users_file_path):
    with open(users_file_path, 'r') as file:
        users_data = json.load(file)

    total_users = len(users_data)
    
    plt.figure(figsize=(5,3))
    plt.bar(['Total Users'], [total_users / 1e6], color='skyblue')
    plt.title('Total Number of Users')
    plt.ylabel('Number of Users (in millions)')
    plt.xticks(['Total Users'])

    # Correctly format the y-axis to display values in millions
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:.1f}M'))
    
    plt.tight_layout()
    plt.show()

    # Note: Save the figure before calling plt.show() to ensure the file is saved properly
    plt.savefig('/home/opc/koo-data/total_users.png')

    print(f"Total number of users: {total_users}")
else:
    print("The file does not exist or the path is incorrect.")



