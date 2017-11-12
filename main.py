import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_name = "datasets/Datasets.xlsx"

data_xls = pd.read_excel(file_name)
data_xls.to_csv("datasets/Datasets.csv", encoding="utf-8", index=False)