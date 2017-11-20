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

class FrequentCustomers(APIView):

    authentication_classes = []
    permission_classes = []



    def get(self, request, format=None):
            # file = "app/Charts/new_sets.csv"
            df = Dataset.df

                
            custID = df["CustomerID"].value_counts().reset_index()
            custID.columns = ["CustID","Items they buyed"]
            custID["CustID"] = custID["CustID"].apply(str)
            custIDx = custID.sort_values("Items they buyed", ascending=False).head(40)
            custIDx=custIDx.head(20)
            x= custIDx['CustID'].tolist()
            y=custIDx['Items they buyed'].tolist()
            data={ "Customer":x,"ItemNo":y,}

            return Response(data)
