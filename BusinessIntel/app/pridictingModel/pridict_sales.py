from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



from ..Charts.Common import CommonData as Dataset
df = Dataset.df


prod_prof = df
prod_prof["TotalAmount"] = prod_prof["Quantity"]*prod_prof["UnitPrice"]
prod_prof["Totalprofit"] = prod_prof["Quantity"]*prod_prof["Profit"]

prod_prof["Totalprofit"].sum() # Anually Sale

prod_prof=prod_prof.set_index("InvoiceDate")

prod_prof.head()
total_amount = prod_prof.groupby("InvoiceDate")["TotalAmount","Quantity","UnitPrice"].agg({"TotalAmount":["sum","count"],
                                                                   "Quantity":["sum","count"],
                                                                   "UnitPrice":["sum","count"]})
total_amount.head()
tA = total_amount["TotalAmount"]["sum"]
tA

prod_prof.index = prod_prof.index.to_datetime()
prod_prof['tA']=tA
prod_prof=prod_prof["tA"]
prod_prof=prod_prof.groupby(prod_prof.index.month).agg('sum')

prod_prof
prod_prof.head()

y = total_amount["TotalAmount"]["sum"].values
X = total_amount[["Quantity","UnitPrice"]].values

train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.30, random_state=415)  # i split the datasets here by 30%

'''This is plotting section'''
# fig, ax = plt.subplots(figsize=(20,8))
# a = total_amount.index[0:div] # this is the date ex: '2010-10-1, 2010-10-2, 2010-10-3'
# ax.plot(a, train_y, "k", label="Train sets", color="green") # i put on the plot for our expected output, this is the color green
# ax.plot(a, yhat, "k--", label="Prediction", color="red") # here is the plot for prediction, this is color red in our plot
# ax.legend(loc="upper right", shadow=True, fontsize=20)
# plt.xticks(rotation="vertical")
# plt.title("Train Prediction", fontsize=30)
# plt.xlabel("Sales in a Months", fontsize=20)
# plt.ylabel("Sale in a Month", fontsize=20)
# plt.show()

test_yhat = svr_lin.predict(test_x)

# fig, ax = plt.subplots(figsize=(20,8))
# a = total_amount.index[div:div_len]
# ax.plot(a, test_y, "k", color="green", label="Train Test")
# ax.plot(a, test_yhat, "k--", color="red", label="Prediction Test")
# ax.legend(loc="upper left", shadow=True, fontsize=20)
# plt.title("Test Prediction", fontsize=30)
# plt.xticks(rotation="vertical")
# plt.xlabel("Months Sale", fontsize=20)
# plt.ylabel("Sale in Month", fontsize=20)
# plt.show()




model=svr_lin

# Dump the trained decision tree classifier with Pickle
filename1 = 'pickle_model1.pkl'
# Open the file to save as pkl file
save_model_pkl = open(filename1, 'wb')
pickle.dump(model, save_model_pkl)
# Close the pickle instances
save_model_pkl.close()


# Loading the saved model pickle
pklfile = open(filename1, 'rb')
load_model = pickle.load(pklfile)
print ("Loaded model :: ", load_model)

# Calculate the accuracy score and predict target values
score = load_model.score(test_x, test_y)  
print("Test score: {0:.2f} %".format(100 * score))  
Ypredict = load_model.predict(train_x) 
Ypredict



