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

class CustomersVSno_of_items(APIView):

    authentication_classes = []
    permission_classes = []



    def get(self, request, format=None):
            # file = "app/Charts/new_sets.csv"
            custID = Dataset.df

            custID["TotalAmount"] = custID["Quantity"]*custID["UnitPrice"]
            custID=custID.groupby(['CustomerID'])['TotalAmount'].sum()
            custID=custID.reset_index().sort_values("TotalAmount", ascending=False).head(30)

            x= custID['CustomerID'].tolist()
            y=custID['TotalAmount'].tolist()

            
            data={ "Customer":x,"TotalAmount":y,}

            return Response(data)
