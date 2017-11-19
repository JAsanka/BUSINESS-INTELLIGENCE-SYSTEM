from django.shortcuts import render,render_to_response
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response


import pandas_highcharts
import pandas as pd
import numpy as np



# for PieChart

class SalesProfitOfYearData(APIView):

    authentication_classes = []
    permission_classes = []
   

    def get(self, request, format=None):
        
        file = "app/Charts/new_sets.csv"
        df = pd.read_csv(file, index_col=0)

        
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
       
#         totalProfit=prod_prof.drop('TotalAmount',1)
#         totalSales=prod_prof.drop('Totalprofit',1)
#         # totalProfit=totalProfit.values.tolist()
        # totalSales=totalSales.values.tolist()
#         totalProfit=totalProfit.to_json(orient='records')
#         totalSales=totalSales.to_json(orient='records')
#         totalSales
        


        data={
                "totalProfit":totalProfit,"totalSales":totalSales ,"months":months
            }

        return Response(data)






