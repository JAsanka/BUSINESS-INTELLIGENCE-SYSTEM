from django.shortcuts import render,render_to_response
from django.template import loader
#from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .Common import CommonData as Dataset


import pandas_highcharts
#from pandas_highcharts.core import serialize
import pandas as pd
import numpy as np



#  bar Chart the items need to be kept and order more quantity and we can answer
#  the question what product most profitable and product to be kept

class indexloadData(APIView):

    authentication_classes = []
    permission_classes = []




    def get(self, request, format=None):


        file = "app/Charts/new_sets.csv"
        df = Dataset.df
        Total_Sessions=df['Logged OS'].count()
        prod_prof = df
        prod_prof["TotalAmount"] = prod_prof["Quantity"]*prod_prof["UnitPrice"]
        prod_prof["Totalprofit"] = prod_prof["Quantity"]*prod_prof["Profit"]
        TotalProfit=prod_prof['Totalprofit'].sum()
        TotalSales=prod_prof['TotalAmount'].sum()

        data={
                "Total_Sessions":Total_Sessions,"TotalProfit":TotalProfit,"TotalSales":TotalSales,
            }

        return Response(data)


