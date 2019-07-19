import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.preprocessing import LabelEncoder



x = pd.read_csv('crime.csv', usecols=[
               'OFFENSE_CODE', 'OFFENSE_CATEGORY_ID', 'GEO_LAT', 'GEO_LON', 'IS_TRAFFIC', 'IS_CRIME'])

x['OFFENSE_CATEGORY_ID'] = LabelEncoder().fit_transform(x['OFFENSE_CATEGORY_ID'])
x = x[pd.notnull(x['GEO_LON'])]
x.to_csv("preprocess.csv", sep=",", encoding='utf-8', index=False)


#y = pd.read_csv('crime.csv', usecols=[
 #              'OFFENSE_CODE', 'OFFENSE_CATEGORY_ID', 'GEO_LAT', 'GEO_LON', 'IS_TRAFFIC', 'IS_CRIME'])

#y['OFFENSE_CATEGORY_ID'] = LabelEncoder().fit_transform(y['OFFENSE_CATEGORY_ID'])
#y = y[pd.notnull(y['GEO_LAT'])]
#y.to_csv("div.csv", sep=",", encoding='utf-8', index=False)




