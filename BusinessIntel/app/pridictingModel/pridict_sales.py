import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

file = "new_sets.csv"
df = pd.read_csv(file, index_col=0, )

from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
total_amount.head()

y = total_amount["TotalAmount"]["sum"].values
X = total_amount[["Quantity","UnitPrice"]].values

train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.30, random_state=415)  # i split the datasets here by 30%

'''I am using the SVR Polynomial from the sklearn model, with iteration by 1000 '''
svr_lin = SVR(kernel="poly", C=1e-5, degree=1, max_iter=1000)
svr_lin.fit(train_x, train_y) # i feed the training sets here to our model
yhat = svr_lin.predict(train_x) # and this is the output or a prediction for our training sets
div = len(train_y) # dont mind this
div_len = len(total_amount) # dont mind this


'''This is plotting section'''
fig, ax = plt.subplots(figsize=(20,8))
a = total_amount.index[0:div] # this is the date ex: '2010-10-1, 2010-10-2, 2010-10-3'
ax.plot(a, train_y, "k", label="Train sets", color="green") # i put on the plot for our expected output, this is the color green
ax.plot(a, yhat, "k--", label="Prediction", color="red") # here is the plot for prediction, this is color red in our plot
ax.legend(loc="upper right", shadow=True, fontsize=20)
plt.xticks(rotation="vertical")
plt.title("Train Prediction", fontsize=30)
plt.xlabel("Sales in a Months", fontsize=20)
plt.ylabel("Sale in a Month", fontsize=20)
plt.show()


test_yhat = svr_lin.predict(test_x)

fig, ax = plt.subplots(figsize=(20,8))
a = total_amount.index[div:div_len]
ax.plot(a, test_y, "k", color="green", label="Train Test")
ax.plot(a, test_yhat, "k--", color="red", label="Prediction Test")
ax.legend(loc="upper left", shadow=True, fontsize=20)
plt.title("Test Prediction", fontsize=30)
plt.xticks(rotation="vertical")
plt.xlabel("Months Sale", fontsize=20)
plt.ylabel("Sale in Month", fontsize=20)
plt.show()