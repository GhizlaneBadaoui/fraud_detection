# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, cross_val_score, train_test_split
from sklearn.tree import DecisionTreeClassifier


X_train = None
X_test = None
y_train= None
y_test= None

model = DecisionTreeClassifier(random_state=0)
grid_search= None

def init():
    file_path = "CalculStatisticMS/src/main/java/Models/clean_data.csv"
    dataset = pd.read_csv(file_path, sep = ";")

    X = dataset.iloc[:, :-1]  # Sélectionner toutes les colonnes sauf la dernière
    Y = dataset.iloc[:, -1]

    # only use the first N samples to limit training time
    num_samples = int(len(X)*0.2)
    X, Y = X[:num_samples], Y[:num_samples]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    print(X_train)
    return "completed"

def train():
    model.fit(X_train,y_train)
    param_grid = {
        'max_depth': [5]
    #    'min_samples_split': [2, 5, 10],
    #    'min_samples_leaf': [1, 2, 4],
    #    'max_features': ['sqrt', 'log2', None],
    #    'criterion': ['gini', 'entropy'],
    #    'splitter' : ['best', 'random'],
    #    'max_leaf_nodes' : [5, 15, 20, 25]
        }

    grid_search = GridSearchCV(DecisionTreeClassifier(random_state=0),param_grid=param_grid,cv=5,scoring='accuracy')
    grid_search.fit(X_train,y_train)

def predict_with_confidence(self, X):
    if hasattr(grid_search.best_estimator_, "predict_proba"):
        probabilities = grid_search.best_estimator_.predict_proba(X)
        predictions = grid_search.best_estimator_.predict(X)
        return [(pred, max(prob)) for pred, prob in zip(predictions, probabilities)]
    else:
        raise ValueError("Ce modèle ne supporte pas la prédiction de probabilités.")


def perf(self):
    cv_scores = cross_val_score(grid_search, X_train, y_train, cv=5).mean()
    print("##########################################################\ncross validataion : ",cv_scores)
    print("accuracy : ",accuracy_score(y_test,grid_search.predict(X_test)))
    print("training score : ",grid_search.score(X_train,y_train))
    print("testing score : ",grid_search.score(X_test,y_test))

print(init())

#################### First iteration  ########################

#cross validataion :  0.7659539057009863
#accuracy :  0.7837116154873164
#training score :  1.0
#testing score :  0.7837116154873164
###########################################################
#cross validataion :  0.814040653039285
#accuracy :  0.8397863818424566
#training score :  0.8282873256159098
#testing score :  0.8397863818424566

