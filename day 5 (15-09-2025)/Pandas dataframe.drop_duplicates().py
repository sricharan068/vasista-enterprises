
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Alice", "David"],
    "Age": [25, 30, 25, 40],
    "City": ["NY", "LA", "NY", "Chicago"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df_cleaned = df.drop_duplicates()

print("\nModified DataFrame (no duplicates)")
print(df_cleaned)

#Dropping Duplicates Based on Specific Columns
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'David'],
    'Age': [25, 30, 25, 40],
    'City': ['NY', 'LA', 'SF', 'Chicago']
})

df_cleaned = df.drop_duplicates(subset=["Name"])

print(df_cleaned)

#Keeping the Last Occurrence of Duplicates
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'David'],
    'Age': [25, 30, 25, 40],
    'City': ['NY', 'LA', 'NY', 'Chicago']
})

df_cleaned= df.drop_duplicates(keep='last')
print(df_cleaned)


#Dropping All Duplicates
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'David'],
    'Age': [25, 30, 25, 40],
    'City': ['NY', 'LA', 'NY', 'Chicago']
})
df_cleaned = df.drop_duplicates(keep=False)
print(df_cleaned)


#Modifying the Original DataFrame Directly
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'David'],
    'Age': [25, 30, 25, 40],
    'City': ['NY', 'LA', 'NY', 'Chicago']
})
df.drop_duplicates(inplace=True)
print(df)


#Dropping Duplicates Based on Partially Identical Columns
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Alice", "David", "Bob"],
    "Age": [25, 30, 25, 40, 30],
    "City": ["NY", "LA", "NY", "Chicago", "LA"]
}

df = pd.DataFrame(data)

df_cleaned = df.drop_duplicates(subset=["Name", "City"])

print(df_cleaned)
