#practical 1 creating, manipulating objects
import pandas as pd
import numpy as np
#create dara frame
data={
    'Name': ['ABC', 'PQR', 'XYZ', 'HIJ'],
    "Age": [19, 21, 24, 34],
    "Salary": [20000, 40000, 30000, 50000]
    }
df = pd.DataFrame(data)
#display the dataframe
print("Initial DataFrame:")
print(df)




