import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import confusion_matrix, classification_report
from flask import Flask, render_template, request


x = pd.read_csv('preprocess.csv', usecols=[
                'OFFENSE_CODE', 'OFFENSE_CATEGORY_ID', 'GEO_LAT', 'GEO_LON'])
y = pd.read_csv('preprocess.csv', usecols=['IS_CRIME'])
print(x)
print(y)
df = pd.read_csv('preprocess.csv', index_col=['OFFENSE_CODE'], usecols=[
    'OFFENSE_CODE', 'OFFENSE_CATEGORY_ID', 'GEO_LAT', 'GEO_LON'])
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=.3, random_state=42)
dtree = tree.DecisionTreeClassifier()

dtree.fit(X_train, y_train.values.ravel())


score2 = dtree.score(X_test, y_test)
print(score2)

result1 = dtree.predict(X_test)
print(confusion_matrix(y_test, result1))
print(classification_report(y_test, result1))


app = Flask(__name__)
@app.route('/')
def crime():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def output():
    if request.method == 'POST':
        o_id = request.form['offense_code']
        oc_id = request.form['offense_category_id']
        lat = request.form['geo_x']
        lon = request.form['geo_y']
        o_id = int(o_id)
        oc_id = int(oc_id)
        lat = float(lat)
        lon = float(lon)
        print(lat)
        print(o_id)
        d = df.loc[o_id]
        d.to_csv("d.csv", sep=",", encoding='utf-8', index=True)
        d = pd.read_csv('d.csv')
        print(d)
        i = 0
        print(len(d.index))
        if oc_id == d['OFFENSE_CATEGORY_ID'][0]:
            for i in range(len(d.index)):
                if lat == d['GEO_LAT'][i] and lon == d['GEO_LON'][i]:
                    result = dtree.predict([[o_id, oc_id, lat, lon]])
                    if "1" in str(result):

                        print(' is 1- crime ')
                        if oc_id == 0:
                            data1 = "aggravatedassault.geojson"
                        elif oc_id == 1:
                            data1 = "allothercrime.geojson"
                        elif oc_id == 2:
                            data1 = "arson.geojson"
                        elif oc_id == 3:
                            data1 = "autotheft.geojson"
                        elif oc_id == 4:
                            data1 = "burglary.geojson"
                        elif oc_id == 5:
                            data1 = "drugalcohol.geojson"
                        elif oc_id == 6:
                            data1 = "larceny.geojson"
                        elif oc_id == 7:
                            data1 = "murder.geojson"
                        elif oc_id == 8:
                            data1 = "othercrimesagainstpersons.geojson"
                        elif oc_id == 9:
                            data1 = "publicdisorder.geojson"
                        elif oc_id == 10:
                            data1 = "robbery.geojson"
                        elif oc_id == 12:
                            data1 = "theftfrommotorvehicle.geojson"
                        elif oc_id == 13:
                            data1 = "trafficaccident.geojson"
                        elif oc_id == 14:
                            data1 = "whitecollarcrime.geojson"
                        else:
                            data1 = "allothercrime.geojson"

                        print(data1)
                        return render_template('result.html', data1=data1)

                    elif "0" in str(result):
                        print(' is 0-not crime')
                        return render_template('result0.html')
        else:
            return render_template('result0.html')
    
    return render_template('result0.html')

if __name__ == '__main__':
    app.run(debug=True)
