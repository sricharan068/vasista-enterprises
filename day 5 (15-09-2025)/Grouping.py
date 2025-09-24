import pandas as pd
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

team = df.groupby('Team')
print(team.first()) # Let's print the first entries in all the groups formed.


grouping = df.groupby(['Team', 'Position'])
print(grouping.first())


aggregated_data = df.groupby(['Team', 'Position']).agg(
    total_salary=('Salary', 'sum'),
    avg_salary=('Salary', 'mean'),
    player_count=('Name', 'count')
)

print(aggregated_data)


df['Rank within Team'] = df.groupby('Team')['Salary'].transform(lambda x: x.rank(ascending=False))
print(df)

sort=df.sort_values(by="Rank within Team")
print(sort)

sort.head(10)
sort.tail(10)
