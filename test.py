import pandas as  pd 
import numpy as np 
import json
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn import tree
from sklearn.preprocessing import LabelEncoder

x=pd.read_csv('_labled.csv', usecols=['OFFENSE_ID','OFFENSE_CATEGORY_ID','GEO_LON','GEO_LAT'])
y=pd.read_csv('_labled.csv',usecols=['IS_CRIME'])
print(x)
print(y)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.9, random_state=42)
clf = tree.DecisionTreeClassifier()
model=clf.fit(X_train,y_train)
predictions = clf.predict(X_test)

print ("Score:", model.score(X_test, y_test))
