import numpy as np
import pandas as pd
from numpy import random

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df=pd.read_csv("sample_data.csv")
print(df)
x=np.array(df["YearsExperience"])
y=np.array(df["Salary"])
x,y

X=np.array([1,2,3])
Y=np.array([4,5,6])
print(np.dot(X,Y))

x_max=x.max()
x_min=x.min()
x_mean=x.mean()
x_std_dev=np.sqrt((np.sum((x-x_mean)*(x-x_mean)))/len(x))

for i in range(len(x)):
    x[i]=(x[i]-x_mean)/x_std_dev

    y_max=y.max()
y_min=y.min()
y_mean=y.mean()
y_std_dev=np.sqrt((np.sum((y-y_mean)*(y-y_mean)))/len(y))

for i in range(len(y)):
    y[i]=(y[i]-y_mean)/y_std_dev

x,y

lr=0.01
epochs=100
w=b=0
for i in range(epochs):
    w_slope= -2*np.dot((y-w*x-b),x)
   
    b_slope=-2*np.sum((y-w*x-b))
    
    w=w-lr*w_slope
    b=b-lr*b_slope
    
x_plot=np.arange(-2,2,0.1)
y_plot=w*x_plot+b
plt.scatter(x,y)
plt.plot(x_plot,y_plot)
plt.show()
