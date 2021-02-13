from typing import List, no_type_check
from sklearn import datasets
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

iris = datasets.load_iris()

x = iris['data'][:,3:]
y = (iris ['target'] ==2).astype(np.int)

#traing logistic classifeir

cls = LogisticRegression()
cls.fit(x,y)
ex = cls.predict([[2.6]])
print(ex)

x_new = np.linspace(0,3,1000).reshape(-1,1)
y_prob = cls.predict_proba(x_new)
plt.plot(x_new,y_prob[:,1], "g-")
plt.show()

# print(list(iris.keys()))
