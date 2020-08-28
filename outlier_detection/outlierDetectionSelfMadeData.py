import pandas as pd
import numpy as np
import seaborn as sns

## Create & Describe Data Frame
df_ = pd.DataFrame({'height':[1,2,3,2,16,3,4,4,3,5,6,2,25],'weight':[3,5,6,17,7,8,7,6,5,6,7,12,22]})

df_.describe()
## Plot Graphs To Identify Outliers
sns.scatterplot(x='weight',y=0, data=df_)
sns.boxplot(x='weight', data=df_)
## Z-Score Function That Return Outliers 
def z_score(x,threshold):
    outliers_zscore = []
    mean,std=np.mean(x),np.std(x)
    for i in x:
        z= (i-mean)/std
        if abs(z)>threshold:
            outliers_zscore.append(i)
    return outliers_zscore

## IQR Method That Returns Outliers
def iqr_range(x,threshold):
    outliers_iqr = []
    q1 = np.percentile(x,25)
    q2 = np.percentile(x,50)
    q3 = np.percentile(x,75)
    iqr = q3-q1
    #print(q1,q2,q3,iqr)
    lower_bound = q1-(iqr*threshold)
    upper_bound = q3+(iqr*threshold)
    print(lower_bound,upper_bound)
    for i in x:
        if i<lower_bound or i>upper_bound:
            outliers_iqr.append(i)
    return outliers_iqr

z_score(df_.weight,2)
iqr_range(df_.weight,1.5)