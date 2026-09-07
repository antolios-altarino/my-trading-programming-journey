
import pandas as pd

# -------------------------------------------------
# Lesson 1: Introduction to Pandas
# What kind of data does Pandas handle? DataFrame
# -------------------------------------------------

# A DataFrame is a 2-dimensional labeled data structure
# with columns that can contain different types of data.
#
# Imagine a table of data with rows and columns.
# Each column can contain a different type of data.
#
# The index is used to identify each row.
# The column names are used to identify each column.

# Example:

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})

# The column names are 'Name', 'Age', and 'City'.
# The index is automatically generated as 0, 1, 2, 3.

print(df)

# Output:
#       Name  Age         City
# 0    Alice   25     New York
# 1      Bob   30  Los Angeles
# 2  Charlie   35      Chicago
# 3    David   40      Houston