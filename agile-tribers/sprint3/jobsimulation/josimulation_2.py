import numpy as np
from scipy import stats
data=[1,2,3,4,5,6,7,8,9,10]
before_training=[52,47,58,43,50,46,49,53,48,51]
after_training=[56,50,60,45,54,48,53,56,51,55]
alpha=0.05
t_stats,p_value=stats.ttest_rel(before_training,after_training)
print("t_stats:",t_stats)
print("p_value:",p_value)
if t_stats < 0:
    onetailed_p_value=p_value/2
    print("onetailed_p_value:",onetailed_p_value)
else:
    onetailed_p_value=1-(p_value/2)
    
if onetailed_p_value > alpha:
    print("No significant improvement, Fail to reject the null hypothesis")
else:
    print("Typing speed significantly improved ,reject the null hypothesis ")
