from django.shortcuts import render,render_to_response
from django.template import loader
#from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


import pandas_highcharts
#from pandas_highcharts.core import serialize
import pandas as pd
import numpy as np

# products_df = pd.read_csv("app/input/products.csv")
# order_products_prior_df = pd.read_csv("app/input/order_products__prior.csv")


class ChartData(APIView):

    authentication_classes = []
    permission_classes = []


    def get(self, request, format=None):
            
            
        # dataset = order_products_prior_df.iloc[:,1:3]
        # dataset['no_of_orders'] = dataset.groupby('product_id')['add_to_cart_order'].transform(sum)
        # dataset=dataset.drop_duplicates('product_id', keep='first', inplace=False)
        # dataset=dataset.drop(['add_to_cart_order'], axis=1)
        # dataset=dataset.sort_values(by='no_of_orders',ascending=False)
        # dataset=dataset.iloc[:20,:]


        # dataset.rename(columns={'product_id': 'product'}, inplace=True)

        # dataset=dataset.join(products_df['product_name'],on='product',rsuffix='_id')
        # dataset=dataset.reset_index(drop=True)

        # productNames=dataset['product_name'].tolist()
        # no_of_orders=dataset['no_of_orders'].tolist()

        productNames=['a','b','c']
        no_of_orders=[1,2,3]

        data={
                "sales":no_of_orders,"customers":productNames,
            }

        return Response(data)
