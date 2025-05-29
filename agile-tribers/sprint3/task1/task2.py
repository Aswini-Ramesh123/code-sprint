#Task 1
#Read csv file
import pandas as pd
url='https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch07/Salaries.csv'
data=pd.read_csv(url)
df=data.head()
print(df)

#program 2
import pandas as pd
data=pd.read_excel("Cars.xlsx")
data.to_csv("Cars.csv",index=False)
df=data.head()
print(df)

#head
import pandas as pd
df=pd.read_csv("Cars.csv")
print(df.head())

#tail
import pandas as pd
df=pd.read_csv("Cars.csv")
print(df.tail())

#shape
import pandas as pd
df=pd.read_csv("Cars.csv")
print(df.shape)

#describe
import pandas as pd
df=pd.read_csv("Cars.csv")
print(df.describe())

#Task 2

import pandas as pd
data={
    "Name":["John","Jane","Babu","Peter","Leju"],
    "Age":[25,30,35,40,55],
    "city":["New York","London","Paris","UK","Germany"]
    }
df=pd.DataFrame(data)
print("DataFrame Creation:")
print(df)
print()
print("To retrieve the first five rows")
print(df.head(5))
print()
print(df.info())

#Task3
import pandas as pd
data=pd.DataFrame({
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR'],
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107],
    'Salary': [50000, 70000, 60000, 52000, 72000, 65000, 51000],
    'YearsOfExperience': [5, 7, 6, 4, 8, 5, 3],
    'Age': [30, 32, 35, 28, 33, 36, 27]
})
print(data.groupby('Department')['Salary'].mean())
print()
print("Multiple columns")
grouped=data.groupby('Department').agg({
    "Salary":['mean','min','max'],
    "YearsOfExperience":['mean','sum'],
    "Age":['mean']
    })
print(grouped)
print()
print()
filter=grouped[grouped[('Salary','mean')]>60000]
print(filter)
print()
custom=data.groupby('Department').agg({
    "Age":['mean'],
    "Salary":['mean']
    })
print(custom)


























