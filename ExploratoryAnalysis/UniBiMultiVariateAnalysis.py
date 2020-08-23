import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_iris = pd.read_csv('../../Data/irisdata.csv')
del df_iris['Id']
df_iris.info()
def univariate(df,column,target):
    fig, ax=plt.subplots(nrows =1,ncols=3,figsize=(20,8))
    sns.set(style="ticks", color_codes=True)
    sns.set(style="darkgrid")
    ax[0].set_title("Scatter Plot")
    sns.scatterplot(x=column,y=0, ax=ax[0],hue=target, data=df)
    ax[1].set_title("Distribution Plot")
    sns.scatterplot(x=column,y=0, ax=ax[1],hue=target, data=df)
    target_setosa = df_iris.loc[df_iris[target]=='Iris-setosa']
    target_versicolor = df_iris.loc[df_iris[target]=='Iris-versicolor']
    target_virginica = df_iris.loc[df_iris[target]=='Iris-virginica']
    sns.distplot(target_setosa[column], ax=ax[1])
    sns.distplot(target_versicolor[column], ax=ax[1])
    sns.distplot(target_virginica[column],ax=ax[1])
    ax[2].set_title("Box Plot")
    sns.boxplot(x='Species', y='SepalLengthCm', data=df_iris, ax=ax[2])

univariate(df_iris,'SepalLengthCm','Species')
univariate(df_iris,'SepalWidthCm','Species')
univariate(df_iris,'PetalLengthCm','Species')
univariate(df_iris,'PetalWidthCm','Species')

def bivariate(df,col1,col2,target):
    fig, ax=plt.subplots(nrows =1,ncols=3,figsize=(20,8))
    sns.set(style="ticks", color_codes=True)
    sns.set(style="darkgrid")
    ax[0].set_title("Scatter Plot")
    sns.scatterplot(x=col1,y=col2, hue=target, data=df_iris, ax=ax[0])
    ax[1].set_title("Line Plot")
    sns.lineplot(x=col1,y=col2, hue=target, data=df_iris, ax=ax[1])
    ax[2].set_title("Violin Plot")
    sns.violinplot(x=col1,y=target,data=df_iris, ax=ax[2])

bivariate(df_iris,'PetalLengthCm','PetalWidthCm','Species')
bivariate(df_iris,'SepalLengthCm','SepalWidthCm','Species')

def multivariate(df, target):
    corr = df.corr()
    sns.pairplot(df,hue=target)
    f, ax = plt.subplots(figsize=(14, 9))
    sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values,annot= True)
    plt.show()

multivariate(df_iris,'Species')