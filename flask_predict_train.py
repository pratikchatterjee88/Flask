# -*- coding: utf-8 -*-
"""
Created on Wed May 26 23:22:29 2021

@author: pratik.chatterjee
"""

# build a Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# loading the data

iris= load_iris()
X=iris.data
y=iris.target

# spliting the data

X_train,X_test, y_train, y_test= train_test_split(X,y,random_state=42, test_size=0.5)

# Build the model
clf=RandomForestClassifier(n_estimators=10)

#Train the classifier
clf.fit(X_train, y_train)

#predictions
predicted=clf.predict(X_test)

#Check accuracy
print(accuracy_score(predicted, y_test))

#pickling
# pickling is the process of saving the python file in binary so that we can load anytime later

import pickle
with open('C:/Users/pratik.chatterjee/OneDrive - Thermo Fisher Scientific (1)/Desktop/Folders/Machine Learning/Deploy ML and NLP models with Dockers/Flask/rf.pkl','wb')as model_pkl:
    pickle.dump(clf,model_pkl)
    
    
    
    
    
    
    
    
    
    
    
    
    