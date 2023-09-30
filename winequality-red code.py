import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
##############################################################
data=pd.read_csv(r'C:\Users\User\OneDrive\Desktop\DS DATA FILES\winequality-red.csv')
data.shape
data.head()
data.tail()
data.info
data.describe()
pd.set_option('display.max_columns',13)
data.isna().sum()
data.columns

##############################################################
data1=pd.read_csv(r'C:\Users\User\OneDrive\Desktop\DS DATA FILES\winequality-red.csv',na_values=[0])
data1.isna().sum()
##############################################################
columns=['citric acid']
for column in columns:
    mean=data[column].mean()
    data[column]=data[column].replace(0,mean)
##############################################################
plt.figure(figsize=(12,8))
sns.pairplot(data)

columns=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'sulphates', 'alcohol', 'quality']
for column in columns:
    plt.figure(figsize=(10,8))
    sns.boxplot(x=data['quality'],y=data[column])
    print('\n')
    
plt.figure(figsize=(12,8))
sns.heatmap(data.corr(),annot=True)
#############################################################
x=data.drop('quality',axis=1)
y=data['quality']

############################################################
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=0)
############################################################
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)
regressor.coef_
regressor.intercept_
y_pred=regressor.predict(x_test)
y_pred
from sklearn import metrics
np.sqrt(metrics.mean_squared_error(y_test,y_pred))
metrics.mean_absolute_error(y_test,y_pred)
metrics.r2_score(y_test,y_pred)
