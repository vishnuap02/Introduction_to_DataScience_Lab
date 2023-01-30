# k-means without built-in

import pandas as pd
from sklearn.model_selection import train_test_split

# 2-clusters k-mean


def predict(df):
    ct = len(df.index())


df = pd.read_csv('diabetes.csv')
print(df.head())
# X = df.drop('Outcome', axis=1)
# get the locations
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.05, random_state=0)
