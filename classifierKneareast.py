from numpy.core.arrayprint import printoptions
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier


iris = datasets.load_iris()
# print(iris.DESCR)

features = iris.data

lables = iris.target
print(features[0], lables[0])

clf = KNeighborsClassifier()

clf.fit(features, lables)

pred = clf.predict([[1,1,1,1]])
print(pred,"prediction")



