from django.shortcuts import render,render_to_response
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response


import pandas_highcharts
import pandas as pd
import numpy as np

from .Common import CommonData as Dataset



# for PieChart

class most_profitable_Products(APIView):

    authentication_classes = []
    permission_classes = []
   

    def get(self, request, format=None):
        
        file = "app/Charts/new_sets.csv"
        df = Dataset.df

        
        prod_prof = df
        prod_prof["TotalAmount"] = prod_prof["Quantity"]*prod_prof["UnitPrice"]
        prod_prof["Totalprofit"] = prod_prof["Quantity"]*prod_prof["Profit"]
        prod_prof=prod_prof.set_index("Description")
        prod_prof = prod_prof['Totalprofit']
        prod_prof

        prod_prof=prod_prof.groupby(prod_prof.index).agg('sum')
        prod_prof.index.names = ['Description']
        prod_prof=prod_prof.reset_index(drop=False)
        
        prod_prof = prod_prof.sort_values("Totalprofit", ascending=False).head(60)
        prod_prof=prod_prof.head(20)
        Description=prod_prof['Description'].tolist()
        Totalprofit=prod_prof['Totalprofit'].tolist()
       

        data={
                "totalProfit":Totalprofit,"description":Description 
            }

        return Response(data)






