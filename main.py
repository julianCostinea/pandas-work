import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', sep=';')
df.columns = [x.lower() for x in df.columns]

mean_budget = df['budget'].mean()

# get client and country with max budget
max_budget = df['budget'].max()
max_budget_index = df['budget'].idxmax()
max_client = df.loc[max_budget_index, 'client']
max_country = df.loc[max_budget_index, 'country']

# client with lowest budget
min_budget = df['budget'].min()
min_budget_index = df['budget'].idxmin()
min_client = df.loc[min_budget_index, 'client']
min_country = df.loc[min_budget_index, 'country']

print(f'Client with highest budget: {max_client}, from {max_country} with budget of {max_budget}')
print(f'Client with lowest budget: {min_client}, from {min_country} with budget of {min_budget}')
print(f'Mean budget: {mean_budget}')

df = df.sort_values(by='budget', ascending=False)
my_plot = plt.legend(df['client'])
df.plot(x='client', y='budget', kind='bar', title='Budget per client')
plt.subplots_adjust(bottom=0.3)
plt.savefig('budget_per_client.png')

# plot = df.plot(x='client', y='budget', kind='bar', title='Budget per client')
# plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.8)
# plot.get_figure().savefig('budget_per_client.png')
