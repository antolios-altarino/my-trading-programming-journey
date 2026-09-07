
import pandas as pd

# -------------------------------------------------------------------
# Lesson 2: Reading and Writing Tabular Data
# How do I read and write tabular data with Pandas?
# read_csv(), to_csv()
# -------------------------------------------------------------------

# Pandas supports many file formats
# (CSV, Excel, SQL, JSON, Parquet, ...).

# Example:
# pd.read_csv() reads a CSV file and creates a DataFrame from it.

df1 = pd.read_csv('lesson_2_read.csv')

print("-------------------------------------------------------------------")
print("This is from lesson_2_read.csv")
print("We read it from a CSV file")
print(df1)

# Output:
#       Name  Age         City
# 0    Alice   25     New York
# 1      Bob   30  Los Angeles
# 2  Charlie   35      Chicago
# 3    David   40      Houston


# Here we create a new DataFrame.

df2 = pd.DataFrame({
    "Name": ["Ali", "Chris"],
    "Age": [26, 20],
    "City": ["Oman", "Los Angeles"]
})

# We save the DataFrame as a CSV file using to_csv().
# index=False prevents Pandas from saving the DataFrame index
# as an extra column in the CSV file.

df2.to_csv('lesson_2_to.csv', index=False)

print("-------------------------------------------------------------------")
print("This is from lesson_2_to.csv")
print("We created the DataFrame and then saved it as a CSV file")
print(df2)
