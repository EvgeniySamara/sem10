import pandas as pd
import random


lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
unique_val = data['whoAmI'].unique()


for val in unique_val:
    data[val] = (data['whoAmI'] == val).astype(int) #true = 1 false = 0
data = data.drop('whoAmI', axis=1)

print(data)
