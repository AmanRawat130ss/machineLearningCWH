import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error


diabetes = datasets.load_diabetes()

# (['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])

# diabetes_X = diabetes.data[:, np.newaxis, 2]
diabetes_X = diabetes.data

diabetes_X_train = diabetes_X[:-30]
diabetes_X_test = diabetes_X[-30:]

diabetes_y_train = diabetes.target[:-30]
diabetes_y_test = diabetes.target[-30:]

model = linear_model.LinearRegression()

model.fit(diabetes_X_train, diabetes_y_train)

diabetes_Y_predict =model.predict(diabetes_X_test)

print("mean square error", mean_squared_error(diabetes_y_test, diabetes_Y_predict))

print("weights : " ,model.coef_)
print("intercept : ", model.intercept_)

# plt.scatter(diabetes_X_test, diabetes_y_test)
# plt.plot(diabetes_X_test,diabetes_Y_predict, 'r')


# plt.show()

