from django.shortcuts import render,render_to_response
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response


import pandas_highcharts
import pandas as pd
import numpy as np

from .Common import CommonData as Dataset



# for PieChart

class SalesProfitOfYearData(APIView):

    authentication_classes = []
    permission_classes = []
   

    def get(self, request, format=None):
        
        file = "app/Charts/new_sets.csv"
        df = Dataset.df

        
        prod_prof = df
        prod_prof["TotalAmount"] = prod_prof["Quantity"]*prod_prof["UnitPrice"]
        prod_prof["Totalprofit"] = prod_prof["Quantity"]*prod_prof["Profit"]
        prod_prof=prod_prof.set_index("InvoiceDate")
        prod_prof = prod_prof[['TotalAmount','Totalprofit']]


        prod_prof.index = prod_prof.index.to_datetime()


        prod_prof=prod_prof.groupby(prod_prof.index.month).agg('sum')
        prod_prof.index.names = ['Date']
        prod_prof=prod_prof.reset_index(drop=False)
        totalProfit=prod_prof['Totalprofit']
        totalSales=prod_prof['TotalAmount']
        months=prod_prof['Date']



        data={
                "totalProfit":totalProfit,"totalSales":totalSales ,"months":months
            }

        return Response(data)






