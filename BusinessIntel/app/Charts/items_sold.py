from django.shortcuts import render,render_to_response
from django.template import loader
#from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


import pandas_highcharts
#from pandas_highcharts.core import serialize
import pandas as pd
import numpy as np



#  bar Chart the items need to be kept and order more quantity and we can answer
#  the question what product most profitable and product to be kept

class itemsSoldData(APIView):

    authentication_classes = []
    permission_classes = []




    def get(self, request, format=None):


        file = "app/Charts/new_sets.csv"
        df = pd.read_csv(file, index_col=0)
        desc = df["Description"].value_counts()
        df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"]).dt.date
        

        productNames=desc.head(40).index
        no_of_orders=desc.head(40).values

        data={
                "no_of_orders":no_of_orders,"productNames":productNames,
            }

        return Response(data)


