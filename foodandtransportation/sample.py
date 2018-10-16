import pandas as pd

df = pd.read_csv('transportationet.csv')
df['assortativity'] = '1'
df['kMax'] = '1'
df['lowerBound'] = '1'
df['graphSize'] = '1'
df.to_csv('samplefile.csv', index=False)
print(df)
