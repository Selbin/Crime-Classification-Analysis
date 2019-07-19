import pandas as pd
y = pd.read_csv('div.csv', index_col=['OFFENSE_CATEGORY_ID'])
arson=y.loc[2]
arson.drop_duplicates(subset =["GEO_LON", "GEO_LAT"], keep = False, inplace = True) 

arson.to_csv("arson.csv", sep=",", encoding='utf-8', index=False)