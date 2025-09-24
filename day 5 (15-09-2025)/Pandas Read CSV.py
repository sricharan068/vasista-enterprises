import pandas as pd

# reading csv file 
df = pd.read_csv('C:\Users\srich\OneDrive\Desktop\vasista\day 5 (20-09-2025)\people_data.csv')
df

df = pd.read_csv("people.csv", usecols=["First Name", "Email"])
print(df)

df = pd.read_csv("people.csv", index_col="First Name")
print(df)

df = pd.read_csv("people.csv", na_values=["N/A", "Unknown"])

import pandas as pd

# Sample data stored in a multi-line string
data = """totalbill_tip, sex:smoker, day_time, size
16.99, 1.01:Female|No, Sun, Dinner, 2
10.34, 1.66, Male, No|Sun:Dinner, 3
21.01:3.5_Male, No:Sun, Dinner, 3
23.68, 3.31, Male|No, Sun_Dinner, 2
24.59:3.61, Female_No, Sun, Dinner, 4
25.29, 4.71|Male, No:Sun, Dinner, 4"""
# Save the data to a CSV file
with open("sample.csv", "w") as file:
    file.write(data)
print(data)

df = pd.read_csv('people.csv', nrows=3)
df

df= pd.read_csv("people.csv")
print("Previous Dataset: ")
print(df)
# using skiprows
df = pd.read_csv("people.csv", skiprows = [4,5])
print("Dataset After skipping rows: ")
print(df)

df = pd.read_csv("people.csv", parse_dates=["Date of birth"])
print(df.info())

