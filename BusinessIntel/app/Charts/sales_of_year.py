from django.shortcuts import render,render_to_response
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response


import pandas_highcharts
import pandas as pd
import numpy as np

from .Common import CommonData as Dataset



class SalesOfYearData(APIView):

    authentication_classes = []
    permission_classes = []
   

    def get(self, request, format=None):
        
        file = "app/Charts/new_sets.csv"
        df = Dataset.df

        inv_data=df.set_index("InvoiceDate")
        inv_data.index = inv_data.index.to_datetime()
        inv_data=inv_data["Quantity"]
        inv_data=inv_data.groupby(inv_data.index.month).agg('sum')
        



        label=inv_data.index
        features=inv_data.values



        data={
                "date":label,"sales":features,
            }

        return Response(data)


