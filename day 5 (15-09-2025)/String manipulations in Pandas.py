import pandas as pd
import numpy as np

data = {'Names': ['Gulshan', 'Shashank', 'Bablu', 'Abhishek', 'Anand', np.nan, 'Pratap'],
        'City': ['Delhi', 'Mumbai', 'Kolkata', 'Delhi', 'Chennai', 'Bangalore', 'Hyderabad']}

df = pd.DataFrame(data)
print(df)


#Change Column Datatype in Pandas
print(df.astype('string'))

#String Manipulations in Pandas
print(df['Names'].str.lower())

print(df['Names'].str.upper())

print(df['Names'].str.strip())

df['Split_Names'] = df['Names'].str.split('a')
print(df[['Names', 'Split_Names']])

print(df['Names'].str.len())

print(df)

print("\nafter using cat:")
print(df['Names'].str.cat(sep=', '))

