import pandas as pd
var=pd.read_csv('C:\\Users\\Gopi\\Desktop\\Data Science\\machine learning\\csv files\\Cars.csv')
var.head()
y=var['MPG']
y
X=var[['HP','VOL','SP','WT']]
X

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X,y)
model.score(X,y)

import pickle
pickle.dump(model,open('final.pkl','wb'))
