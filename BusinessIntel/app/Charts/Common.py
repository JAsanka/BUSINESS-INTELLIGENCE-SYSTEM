import pandas as pd
import numpy as np



class CommonData():

    file = "app/Charts/new_sets.csv"
    df = pd.read_csv(file, index_col=0)