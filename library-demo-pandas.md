# Library Demo: Pandas

```python
import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['John', 'Jane', 'Steve', 'Linda'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Paris', 'London', 'Sydney']
}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Accessing columns
print("\nAccessing columns:")
print(df['Name'])
print(df.Age)

# Accessing rows
print("\nAccessing rows:")
print(df.loc[1])
print(df.iloc[2])

# Filtering data
print("\nFiltering data:")
filtered_df = df[df['Age'] > 30]
print(filtered_df)

# Adding a new column
df['Profession'] = ['Engineer', 'Artist', 'Doctor', 'Teacher']
print("\nDataFrame with a new column:")
print(df)

# Sorting the DataFrame
sorted_df = df.sort_values(by='Age')
print("\nSorted DataFrame:")
print(sorted_df)

# Aggregating data
print("\nAggregated data:")
mean_age = df['Age'].mean()
print("Mean Age:", mean_age)
max_age = df['Age'].max()
print("Max Age:", max_age)

# Grouping data
grouped_df = df.groupby('City').mean()
print("\nGrouped DataFrame:")
print(grouped_df)
```

This script demonstrates various capabilities of Pandas:

- Creating a DataFrame from a dictionary.
- Accessing columns and rows in a DataFrame.
- Filtering data based on a condition.
- Adding a new column to a DataFrame.
- Sorting the DataFrame by a specific column.
- Aggregating data using functions like mean and max.
- Grouping data based on a column.

You can run this script in any Python environment with Pandas installed to see the output. Remember to import the Pandas library (`import pandas as pd`) before running the script.
