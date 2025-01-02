'''
    This is a comprehensive analysis on a transactional data from
    01/12/2010 to 09/12/2011, for a UK-based online retail store
'''

import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv('../../data/cleaned-data.csv')

# correlation between item quantities and unit price
import seaborn as sns

#plt.scatter(df['Quantity'], df['UnitPrice'])

sns.heatmap(df[['Quantity', 'UnitPrice']], annot=True, cmap='coolwarm', linewidths=0.5)

plt.title('Correlation Plot: Quantity vs UnitPrice')
plt.xlabel('Quantity')
plt.ylabel('Unit Price')
#plt.grid(True)
plt.tight_layout()
plt.savefig('../../figures/EDA/scatter plot - heatmap.jpg')
