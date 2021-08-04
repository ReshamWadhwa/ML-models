from sklearn.linear_model import LogisticRegression
import pandas as pd

from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score


lr_library = LogisticRegression(max_iter=1000)

## READING DATA FILES
train = pd.read_csv("../../../data/titanic/train.csv")
print(train.head())

test = pd.read_csv("../../../data/titanic/test.csv")
print(test.head())

# outcome = survived

print(train.describe())
print(train.columns)

X_train = train[['Age','Fare']]
Y_train = train['Survived']
print(X_train.describe())
X_train.loc[X_train.Age.isna(),'Age']=X_train.Age.mean()


X_test = train[['Age','Fare']]
Y_test = train['Survived']
X_test.loc[X_test.Age.isna(),'Age']=X_train.Age.mean()
print(X_train.describe())

lr_library.fit(X_train,Y_train)

y_pred_train = lr_library.predict(X_train)
y_pred_test = lr_library.predict(X_test)

error= pd.DataFrame()
error['y_train']=Y_train
error['pred_y_train']=y_pred_train

error['y_test']=Y_test.astype(float)
error['pred_y_test']=y_pred_test

print(error.describe())
print(error)
print(lr_library.__class__.__name__+" accuracy is %2.3f" % accuracy_score(error['y_test'], y_pred_test))


