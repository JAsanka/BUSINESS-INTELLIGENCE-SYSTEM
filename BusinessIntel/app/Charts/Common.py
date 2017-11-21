import pandas as pd
import numpy as np
#import MySQLdb as sql



class CommonData():

    file = "app/Charts/new_sets.csv"
    df = pd.read_csv(file, index_col=0)

    
    # mysql_cn= sql.connect(host='localhost', 
    #                 port=3306,user='root', passwd='123', 
    #                 db='mysamplesite')
    # df = pd.read_sql('select * from Bisystem;', con=mysql_cn)

    # mysql_cn.close()
    # # df=df.drop(df.columns[[0]], axis=1) 
    # df.rename(columns={'LoggedOS': 'Logged OS'}, inplace=True)
    # print(df)

   