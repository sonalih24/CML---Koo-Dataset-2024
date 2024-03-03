import matplotlib.pyplot as plt

data = {
    'Totals': ['Users', 'Likes', 'Comments', 'Posts', 'Shares'],
    'Count': [1_430_523, 283_591_311, 59_874_490, 71_709_393, 40_055_428]
}

fig, ax = plt.subplots(figsize=(8, 3))  
ax.axis('off')  

table_data = [[total, f"{count:,}"] for total, count in zip(data['Totals'], data['Count'])]

table = plt.table(cellText=table_data, colLabels=['Totals', 'Count'], loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10) 
table.scale(1.2, 1.2)  
plt.show()
plt.savefig('/home/opc/koo-data/! Results & Graphs/koo_data_summary_table.png')





