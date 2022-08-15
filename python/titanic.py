import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier


df =  pd.read_csv('/Users/kurtbembridge/Downloads/train.csv')
test_data =  pd.read_csv('/Users/kurtbembridge/Downloads/test.csv')

df.columns
df = df.dropna(subset=['Age'])



y = df["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch", 'Age', 'Fare']

X = pd.get_dummies(df[features])
X = X.dropna()
X_test = pd.get_dummies(test_data[features])

model = RandomForestRegressor(n_estimators=100, criterion='mae', random_state=0)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('my_submission.csv', index=False)
print("Your submission was successfully saved!")


neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)
