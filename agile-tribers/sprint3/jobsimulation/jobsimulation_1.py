import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_excel("sales_data_with_discounts.xlsx")
volume=data['Volume'].agg({
    'volume_mean' : 'mean',
    'volume_median' : 'median',
    'volume_mode' : lambda x:x.mode()[0],
    'volume_std' : 'std'
    })
print(volume)
print()
price=data['Avg Price'].agg({
    'price_mean' : 'mean',  
    'price_median' : 'median',
    'price_mode' : lambda x:x.mode()[0],
    'price_std' : 'std'
    })
print(price)
print()
sales=data['Total Sales Value'].agg({
    'sales_mean' : 'mean',
    'sales_median' : 'median',
    'sales_mode' : lambda x:x.mode()[0],
    'sales_std' : 'std'
    })
print(sales)
print()
discount_rate=data['Discount Rate (%)'].agg({
    'discount_rate_mean' : 'mean',  
    'discount_rate_median' : 'median',
    'discount_rate_mode' : lambda x:x.mode()[0],
    'discount_rate_std' : 'std'
    })
print(discount_rate)
print()
discount=data['Discount Amount'].agg({
    'discount_mean' : 'mean',  
    'discount_median' : 'median',
    'discount_mode' : lambda x:x.mode()[0],
    'discount_std' : 'std'
    })
print(discount)
print()
net_sales=data['Net Sales Value'].agg({
    'net_sales_mean' : 'mean',  
    'net_sales_median' : 'median',
    'net_sales_mode' : lambda x:x.mode()[0],
    'net_sales_std' : 'std'
    })
print(net_sales)

#data visualization
# Histograms
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_excel('sales_data_with_discounts.xlsx')
numerical_columns=data.select_dtypes(include=['number']).columns
intervals=[0,1000,3000,5000,7000,9000,11000,13000,15000,17000]
for val in numerical_columns:
    plt.figure(figsize=(8,4))
    plt.hist(data[val],bins=intervals,color='green',edgecolor='black')
    plt.title(f'Histogram of {val}')
    plt.xlabel('intervals')
    plt.ylabel('frequencies')
    plt.xticks(intervals,rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()
#box plots
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_excel("sales_data_with_discounts.xlsx")
numerical_data = data.select_dtypes(include='number')
plt.figure(figsize=(10, 8))
sns.boxplot(data=numerical_data, orient="h", palette="Set3")
plt.title("Box Plots for Numerical Variables")
plt.xlabel("Value Range")
plt.tight_layout()
plt.show()
print("Outliers detected in each numerical column:\n")
for column in numerical_data.columns:
    Q1 = numerical_data[column].quantile(0.25)
    Q3 = numerical_data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = numerical_data[(numerical_data[column] < lower_bound) | (numerical_data[column] > upper_bound)]
    print(f"{column}: {len(outliers)} outlier(s)")
    if not outliers.empty:
        print(outliers[[column]].head(), "\n")

#bar chats
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel("sales_data_with_discounts.xlsx")
category_column=data.select_dtypes(include=['object','category']).columns
for col in category_column:
    plt.figure(figsize=(8,5))
    value=data[col].value_counts()
    plt.bar(value.index,value.values)
    plt.xlabel('columns')
    plt.ylabel('counts')
    plt.xticks(rotation=55)
    plt.tight_layout()
    plt.show()


# Standardization of numerical variable
from scipy import stats
import numpy as np
import pandas as pd
data=pd.read_excel("sales_data_with_discounts.xlsx")
lst=[data['Volume'],data['Avg Price'],data['Total Sales Value'],data['Discount Amount'],data['Net Sales Value']]
for i in lst:
    x=i
    
    pop_mean=np.mean(i)
    pop_std=np.std(i)
    z_score=(i-pop_mean)/pop_std
print("Original Data:\n", data.describe())
print("\nz_score Data:\n", z_score.describe())

#Conversion of categorical data into dummy variables
import pandas as pd
data=pd.read_excel("sales_data_with_discounts.xlsx")
categorical_cols = data.select_dtypes(include=['object', 'category']).columns
dummy=pd.get_dummies(data,columns=categorical_cols,drop_first=False)
for col in dummy.columns:
    if dummy[col].dtype == 'bool':
        dummy[col] = dummy[col].astype(int)
print(dummy)

#Task 2
import numpy as np
from scipy import stats
data=[5.1, 4.9, 5.3, 5.0, 4.7, 5.2, 4.8, 5.1, 5.0, 4.9, 5.2, 4.6]
pop_mean=5.5
samp_mean=np.mean(data)
samp_std=np.std(data,ddof=1)
n=12
df=n-1
alpha=0.05
t_stats=(samp_mean-pop_mean)/(samp_std/np.sqrt(n))
t_critical=stats.t.ppf(alpha,df)
print("t_critical:",t_critical)
if t_stats < t_critical:
    print("Reject the null hypothesis, there is sufficient evidence to support the analyst")
else:
    print("Fail to reject null hypothesis, there is sufficient evidence to support the analyst")



    
























