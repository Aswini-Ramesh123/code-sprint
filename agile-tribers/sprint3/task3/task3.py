#task_1
# descriptive statistics
import pandas as pd
data=pd.read_excel("titanic.xlsx")
data.to_csv("titanic.cvs",index=False)
age_mean=data['Age'].mean()
print("Mean:",age_mean)
fare_median=data['Fare'].median()
print("Median:",fare_median)
embarkation_point=data['Embarked'].mode()
print("Mode:",embarkation_point)
fares=data.groupby('Pclass')['Fare'].agg(
    Mean='mean',
    Median='median',
    Mode=lambda x: x.mode()
    )    
print(fares)
aboard=data['SibSp'].agg(
    sMean='mean',
    sMedian='median'
    )
print(aboard)

#skewness and Kurtosis
import pandas as pd
from scipy.stats import kurtosis
data=pd.read_excel("titanic.xlsx")
data.to_csv("titanic.csv")
Mean=data['Fare'].mean()
Median=data['Fare'].median()
Mode=data['Fare'].mode()[0]
skewness=data['Fare'].skew()
if skewness > 0:
    print(f"{skewness} is positive")
elif skewness < 0:
    print(f"{skewness} is negative")

        
age_kurto=kurtosis(data['Age'].dropna(),fisher=False)
if age_kurto > 0:
    print("Lepto Distribution")
elif age_kurto < 0:
    print("Platy Distribution")
elif age_kurto == 0:
    print("Mesokurtic Distribution")

parch_skew=data['Parch'].skew()
if parch_skew == 0:
    print(f"{parch_skew} Symmetrically Distributed")
else:
    print(f"{parch_skew} Not Symmetrically Distributed")



survey1=data['Survived'].skew()
if survey1==0:
    print(f"{survey1} is Symmetrically Distributed")
else:
    print(f"{survey1} is not Symmetrically Distributed")
survey2=data['Survived'].kurtosis()
if survey2==0:
    print(f"{survey2} is not Symmetrically Distributed")
else:
    print(f"{survey2} is not Symmetrically Distributed")


skew_fare=data['Fare'].dropna().skew()
skew_age=data['Age'].dropna().skew()
kurto_fare=data['Fare'].dropna().kurtosis()
kurto_age=data['Age'].dropna().kurtosis()
if kurto_age > kurto_fare:
    print("Kurtosis age have an Extreme Value")
elif kurto_fare > kurto_age:
    print("Kurtosis fare have an Extreme Value")
else:
    print("They are equal values")
if skew_age > skew_fare:
    print("Skewness age have an Extreme Value")
elif skew_fare > skew_age:
    print("skewess fare have an Extreme Value")
else:
    print("They are equal values")


#task 2
#standardization
import pandas as pd
import numpy as np
exp=np.array([1,2,3,4,5])
salary=np.array([1000,2500,4000,5000,7000])
#step 2
mean_exp=exp.mean(axis=0)
std_exp=exp.std(axis=0)
mean_salary=salary.mean(axis=0)
std_salary=salary.std(axis=0)
#step 4
standardized_exp =(exp-mean_exp)/std_exp
standardized_salary=(salary-mean_salary)/std_salary
#step 5
data=pd.DataFrame({
    'exp':[1,2,3,4,5],
    'salary':[1000,2500,4000,5000,7000],
    'standardized_exp':standardized_exp,
    'standardized_salary':standardized_salary
    })
#step 6
e_Mean=np.mean(standardized_exp)
e_Std=np.std(standardized_exp)
s_Mean=np.mean(standardized_salary)
s_Std=np.std(standardized_salary)
print(data)
print("Mean of standardized_exp:",e_Mean)
print("Std of standardized_exp:",e_Std)
print("Mean of standardized_salary:",s_Mean)
print("Std of standardized_salary:",s_Std)


#Task 3
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
data=stats.norm.rvs(loc=50,scale=20,size=5)
df=pd.DataFrame(data,columns=['values'])
print(df)
df['values'].plot.density()
plt.title("Density curve of the dataset")
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()
print("Mean:",df.mean())
print("Median:",df.median())
#task_4
#hypothesis_testing
#program_1
'''import numpy as np
from scipy import stats
pop_mean=168
pop_sd=3.9
n=36
sam_mean=169.5
confidence=0.95
se=pop_sd/np.sqrt(n)
z_score=(sam_mean-pop_mean)/se
print(f"Z_score: {z_score:.3f}")
me=pop_sd/np.sqrt(n)
z_critical=stats.norm.ppf(1-(1-confidence)/2)
print(f"Z_critical: {z_critical:.3f}")
ci=z_critical*me
print(f"CI: {ci:.3f}")
upper=sam_mean+ci
print(f"Upper: {upper:.3f}")
lower=sam_mean-ci
print(f"Lower: {lower:.3f}")
if abs(z_score) > z_critical:
    print("Reject Null hypothesis, there is an difference in height")
else:
    print("Fail to Reject Null hypothesis, there is an no difference in height")'''




#program_2
import numpy as np
from scipy import stats
pop_sd=5.6
n=40
sample_mean=32
confidence_interval=[0.80,0.90,0.98]
#step 1
df=n-1
for confidence in confidence_interval:
    #step 2
    me=pop_sd/np.sqrt(n)
    #z_value
    z_critical=stats.norm.ppf(1-(1-confidence)/2)
    ci=z_critical*me
    lower=sample_mean-ci
    upper=sample_mean+ci
    print(f"\nConfidence Level: {int(confidence*100)}%")
    print(f"z_critical: {z_critical:.3f}")
    print(f"Confidence Interval: {ci:.3f}")
    print(f"Lower_limit: {lower:.3f}")
    print(f"Upper_Limit: {upper:.3f}")
        

#task 5_1
from scipy import stats
import numpy as np
population_mean=100
sample_mean=140
std_mean=20
n_sample=30
np.random.seed(0)
sample_data=np.random.normal(loc=sample_mean,scale=std_mean,size=n_sample)
t_statistics,p_value=stats.ttest_1samp(sample_data,population_mean)
df=n_sample-1
print(f"t_statistics: {t_statistics:.3f}")
print(f"p_value: {p_value:.3f}")
print("DF:",df)
if p_value > 0.05:
    print("Fail to Reject Null Hypothesis,There is No effect in New Medication")
else:
    print("Reject Null Hypothesis,There is effect in New Medication")

#task 5_2
import numpy as np
from scipy import stats
n=15
sample_mean=20
sample_sd=3.5
confidence=0.95
# 15<30 use t_distribution
#step 1
df=n-1
#step 2  t_value
me=sample_sd/np.sqrt(n)
t_critical=stats.t.ppf(1-(1-confidence)/2,df)
ci=t_critical * me
lower=sample_mean-ci
upper=sample_mean+ci
print(f"t_critical : {t_critical:.3f}")
print(f"lower : {lower:.3f}")
print(f"upper : {upper:.3f}")















