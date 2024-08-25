
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

iris = pd.read_csv('sampleData.csv')

x = iris.drop('species', axis=1)
y = iris.species
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=5)

# K Neighbour Classifier
knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
knn.fit(x_train, y_train)
knn_accuracy = knn.score(x_test, y_test)
print("K Neighbors Classifier Accuracy:", knn_accuracy)

#  Logistic Regression
logreg = LogisticRegression()
logreg.fit(x_train, y_train)
y_pred_logreg = logreg.predict(x_test)
logreg_accuracy = metrics.accuracy_score(y_test, y_pred_logreg)
print("Logistic Regression Accuracy:", logreg_accuracy)

# SVM (Support Vector Machine)
svm = SVC(kernel='rbf', random_state=0, gamma=.10, C=1.0)
svm.fit(x_train, y_train)
svm_accuracy = svm.score(x_test, y_test)
print("SVM Accuracy:", svm_accuracy)

# Decision Tree Classifier
dtree = DecisionTreeClassifier()
dtree.fit(x_train, y_train)
dtree_accuracy = dtree.score(x_test, y_test)
print("Decision Tree Classifier Accuracy:", dtree_accuracy)
