'''
    This is a comprehensive analysis on a transactional data from
    01/12/2010 to 09/12/2011, for a UK-based online retail store
'''

import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv('../../data/cleaned-data.csv')

# items that yield high returns (first ten)
valuable_items =df.groupby('Description').agg({
    'Quantity': 'sum',
    'TotalPrice': 'sum'
}).nlargest(10, 'TotalPrice')

valuable_items.plot(kind='bar')
plt.xlabel('Item')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45, ha='right', va='top')
plt.title('Top 10 Most Valuable Items')
plt.tight_layout()
plt.savefig('../../figures/EDA/valuable-items.jpg')
