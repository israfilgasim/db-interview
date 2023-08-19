countries = ['United States', 'United Kingdom', 'Vietnam', 'France', 'Germany', 'Japan', 'China']
capitals = ['Washington', 'London', 'Hanoi', 'Paris', 'Berlin', 'Tokyo', 'Beijing']
population = [328, 67, 97, 67, 83, 126, 1394]
area = [9.834, 0.242, 0.331, 0.643, 0.357, 0.377, 9.597]
gdp = [20580, 29405, 261, 2583, 3949, 4936, 13608]

import pandas as pd
import numpy as np

my_dict = {'country': countries, 'capital': capitals, 'population': population, 'area': area, 'gdp': gdp}
df = pd.DataFrame(my_dict)
row_labels = ['US', 'UK', 'VN', 'FR', 'DE', 'JP', 'CN']
df.index = row_labels



print(df.head()) # print first 5 rows
print(df.info()) # print info of dataframe
print(df.shape) # print shape of dataframe
print(df.describe()) # print statistical info of dataframe
print(df.values) # print values of dataframe
print(df.columns) # print columns of dataframe
print(df.index) # print index of dataframe

# sorting

print(df.sort_values(['population', 'area'], ascending=[False, False])) # sort by population


print(df['area'] > 1) # print true or false
print(df[df['area'] > 1]) # print dataframe with area > 1
print(df['capital'].isin(['London', 'Paris'])) # check if capital is in list

# add new column

df['density'] = df['population'] / df['area']
print(df)


# min, max, mean, median, std, var

print(df['population'].min())
print(df['population'].max())
print(df['population'].mean())
print(df['population'].median())
print(df['population'].std())
print(df['population'].var())
print(df['population'].quantile(0.75))

# cummin, cummax, cumsum, cumprod

print(df['population'].cummin())
print(df['population'].cummax())
print(df['population'].cumsum())
print(df['population'].cumprod())

# value_counts

print(df['capital'].value_counts()) # count number of each capital

# groupby

print(df.groupby('capital')['population'].mean()) # group by capital and calculate mean of population

# set_index and reset_index
print(df)
print(df.set_index('capital')) # set capital as index
print(df.reset_index(drop=True)) # reset index, drop=True means drop old index

# multi-index

df = df.set_index(['country', 'capital'])
print(df)
# df = df.loc[[('United States', 'Washington'), ('United Kingdom', 'London')]]
# print(df)

# sort index

df = df.sort_index()
print(df)
print(df.sort_index(level=['country', 'capital'], ascending=[False, True]))