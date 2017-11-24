from django.shortcuts import render,render_to_response
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
import numpy as np


class Recommendations(APIView):

    authentication_classes = []
    permission_classes = []




    def get(self, request, format=None):
        
        file = "app/pridictingModel/new_sets.csv"
        df = pd.read_csv(file, index_col=0)

        df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"]).dt.date

        prod_prof = df
        prod_prof["TotalAmount"] = prod_prof["Quantity"]*prod_prof["UnitPrice"]

        prod_prof["TotalAmount"].sum() # Anually Sale
        monthly_prod = prod_prof[["InvoiceDate",'CustomerID',"Description"]]

        start_date = "2010-12-01" # YYYY-MM-DD
        end_date = "2010-12-02" # YYYY-MM-DD

        def monthly_sale(start_date, end_date, item):
            ta = monthly_prod

            mask = (ta["InvoiceDate"] > np.datetime64(start_date)) & (ta["InvoiceDate"] <= np.datetime64(end_date))
            monthly_ta = ta[mask]
            prod_ = monthly_ta["Description"].value_counts().sort_values(ascending=False)
            prod = prod_.head(20)
            cusID = monthly_ta["CustomerID"].value_counts()

            cols = prod_.index
            index = cusID.index
            cor_item = pd.DataFrame(index=index, columns=cols)
            cor_item = cor_item.fillna(0)

            for x in monthly_ta[['CustomerID','Description']].dropna().values:
                cor_item.loc[x[0]][x[1]] = 1

            cor = cor_item.corr()
            cor_x = cor[item].sort_values(ascending=False).head(20)

            x_cor=cor_x.index.tolist()
            y_cor=cor_x.values.tolist()
            x_sold,y_sold=prod.index, prod.values
            return (x_cor,y_cor,x_sold,y_sold)

        x_cor,y_cor,x_sold,y_sold=monthly_sale(start_date, end_date, item="HAND WARMER UNION JACK")  
        




        data={
        'x_cor':x_cor,'y_cor':y_cor,
        # 'x_sold':x_sold,'y_sold':y_sold
        }

        return Response(data)

