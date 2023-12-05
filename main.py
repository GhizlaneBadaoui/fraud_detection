import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, cross_val_score, train_test_split
from sklearn.tree import DecisionTreeClassifier

file_path = "./selected_data.csv"
dataset = pd.read_csv(file_path)


X = dataset.iloc[:, :-1]  # Sélectionner toutes les colonnes sauf la dernière
Y = dataset.iloc[:, -1]

# only use the first N samples to limit training time
num_samples = int(len(X)*0.2)
X, Y = X[:num_samples], Y[:num_samples]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=0)
model.fit(X_train,y_train)

cv_scores = cross_val_score(DecisionTreeClassifier(),X_train,y_train,cv=5).mean()
print("cross validataion : ",cv_scores)
print("accuracy : ",accuracy_score(y_test,model.predict(X_test)))
print("training score : ",model.score(X_train,y_train))
print("testing score : ",model.score(X_test,y_test))
param_grid = { 
    'max_depth': [5, 10, 15, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2', None],
    'criterion': ['gini', 'entropy'],
    'splitter' : ['best', 'random'],
    'max_leaf_nodes' : [5, 15, 20, 25]
    }

grid_search = GridSearchCV(DecisionTreeClassifier(random_state=0),param_grid=param_grid,cv=5,scoring='accuracy')

grid_search.fit(X_train,y_train)

cv_scores = cross_val_score(grid_search, X_train, y_train, cv=5).mean()

print("##########################################################\ncross validataion : ",cv_scores)
print("accuracy : ",accuracy_score(y_test,grid_search.predict(X_test)))
print("training score : ",grid_search.score(X_train,y_train))
print("testing score : ",grid_search.score(X_test,y_test))

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

