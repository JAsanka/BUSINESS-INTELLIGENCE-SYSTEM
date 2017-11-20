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

prod_prof.head()

corr = pd.read_csv("datasets//correlation.zip", index_col=0, compression="zip")
corr.head()

cor_ = corr.corr()
corr.columns

def corr_items(item):
    list_item = cor_[item].sort_values(ascending=False).head(10)
    plt.figure(figsize=(12,8))
    sns.barplot(list_item.index, list_item.values)
    plt.title("Correlated Items", fontsize=30)
    plt.xlabel("Items", fontsize=20)
    plt.ylabel("Percentage of correlate", fontsize=20)
    plt.xticks(rotation="vertical")
    plt.show()
    return

item = "FIRE POLISHED GLASS NECKL GOLD"
corr_items(item)