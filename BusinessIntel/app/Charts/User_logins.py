from django.shortcuts import render,render_to_response
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response


import pandas_highcharts
import pandas as pd
import numpy as np



class loginDeviceData(APIView):

    authentication_classes = []
    permission_classes = []
   

    def get(self, request, format=None):
        
        file = "app/Charts/new_sets.csv"
        df = pd.read_csv(file, index_col=0)

        loggedDevice=df['Logged OS']
        loggedDevice=loggedDevice.groupby(loggedDevice.values).size()
        loggedDevice=loggedDevice.reset_index(drop=False)
        loggedDevice.columns = ["Logged OS","Count"]
        os=loggedDevice['Logged OS'].tolist()
        count=loggedDevice['Count'].tolist()

        data={
                "os":os,"count":count,
            }

        return Response(data)


