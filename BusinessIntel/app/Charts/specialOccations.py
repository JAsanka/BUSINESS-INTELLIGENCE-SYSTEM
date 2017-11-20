from django.shortcuts import render,render_to_response
from django.template import loader
#from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


import pandas_highcharts
#from pandas_highcharts.core import serialize
import pandas as pd
import numpy as np

class specialOccationData(APIView):

    authentication_classes = []
    permission_classes = []


    def get(self, request, format=None):


        file = "app/Charts/new_sets.csv"
        df = pd.read_csv(file, index_col=0)
                    
                    
            # -------------------------------------------------------------------------------

            start_date = "2011-01-01" # YYYY-MM-DD
            end_date = "2011-02-20" # YYYY-MM-DD

            prod_prof = df
            prod_prof["TotalAmount"] = prod_prof["Quantity"]*prod_prof["UnitPrice"]
            prod_prof.head()

            prod_prof["TotalAmount"].sum() # Anually Sale   
            total_amount = prod_prof.groupby("Description")["TotalAmount","Quantity","InvoiceDate"].agg({"TotalAmount":["sum","count"],
                                                                            "Quantity":["sum","count"],
                                                                            })
            total_amount.head()



            def monthly_sale(start_date, end_date):
                ta = total_amount
                mask = (ta.index > np.datetime64(start_date)) & (ta.index <= np.datetime64(end_date))
                out=ta[mask]["TotalAmount"]["sum"]

                # plt.figure(figsize=(12,8))
                # ta[mask]["TotalAmount"]["sum"].plot()
                # plt.xlabel("Lenght of Days", fontsize=20)
                # plt.ylabel("Total Sale", fontsize=20)
                # plt.title("Summary for Selected Date", fontsize=30)
                # plt.xticks(rotation="vertical")
                # plt.show()

                return out

            print=monthly_sale(start_date, end_date)

            # -------------------------------------------------------------------------------

        data={
                "Total_Sessions":Total_Sessions,"TotalProfit":TotalProfit,"TotalSales":TotalSales,
            }

        return Response(data)



