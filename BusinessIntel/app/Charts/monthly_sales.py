from django.shortcuts import render,render_to_response
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response


import pandas_highcharts
import pandas as pd
import numpy as np

from .Common import CommonData as Dataset




class SalesOfMonthData(APIView):

    authentication_classes = []
    permission_classes = []
   

    def get(self, request, format=None):
        
        # file = "app/Charts/new_sets.csv"
        df = Dataset.df

#         prod_prof = df
#         prod_prof["TotalAmount"] = prod_prof["Quantity"]*prod_prof["UnitPrice"]
#         prod_prof.head()
#         prod_prof["TotalAmount"].sum() # Anually Sale
#         total_amount = prod_prof.groupby("InvoiceDate")["TotalAmount","Quantity","UnitPrice"].agg({"TotalAmount":["sum","count"],
#                                                                         "Quantity":["sum","count"],
# "UnitPrice":["sum","count"]})




        inv_data=df.set_index("InvoiceDate")
        inv_data.index = inv_data.index.to_datetime()
        inv_data=inv_data["Quantity"]
        inv_data=inv_data.groupby(inv_data.index.month).agg('sum')

        label=inv_data.index
        features=inv_data.values

       
      
# plt.figure(figsize=(12,8))        
# tA.plot()
# plt.xticks(rotation="vertical")
# plt.title("Sale Every Month", fontsize=20)
# plt.xlabel("Year", fontsize=15)
# plt.ylabel("Total Sale", fontsize=15)
# plt.show()


        data={
                "date":label,"sales":features,
            }

        return Response(data)


