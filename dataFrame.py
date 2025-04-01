#practical 1 creating, manipulating objects
import pandas as pd
import numpy as np
#create dara frame
#data: This is a dictionary in Python, which consists of key-value pairs.
data={
    'Name': ['ABC', 'PQR', 'XYZ', 'HIJ'],
    "Age": [19, 21, 24, 34],
    "Salary": [20000, 40000, 30000, 50000]
    }
df = pd.DataFrame(data)   #DataFrame function of pandas is used to create a tabular structure
#display the dataframe
print("Initial DataFrame:")
print(df)

# output
# Initial Datafram
#   Name  Age  Salary
# 0  abc   23   20000
# 1  pqr   43   30000
# 2  xyz   21   50000
# 3  hij   32   40000


# manipulating dataframe : adding new column 
df["Experience"] = [2, 5, 1, 10]  #years of experience
print("\nDtataFrame after adding 'Experience' column:")
print(df)

# output
# Dataframe after adding new column
#   Name  Age  Salary  Experience
# 0  ABC   19   20000           2
# 1  PQR   21   40000           4
# 2  XYZ   24   30000           1
# 3  HIJ   34   50000           3


# manipulating DataFrame: Calculating new column based on existing data
df["Salary_per_year"] = df["Salary"] / df["Experience"]
print("\nDataFrame after calulating 'Salary per year':")
print(df)