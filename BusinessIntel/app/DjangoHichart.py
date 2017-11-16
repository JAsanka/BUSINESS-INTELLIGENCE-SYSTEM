from django.shortcuts import render,render_to_response
from django.template import loader
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response




import pandas_highcharts
from pandas_highcharts.core import serialize
import pandas as pd
import numpy as np

# products_df = pd.read_csv("app/input/products.csv")
# order_products_prior_df = pd.read_csv("app/input/order_products__prior.csv")

def hichartGenerate(request, format=None):
    # dataset = order_products_prior_df.iloc[:,1:3]
    # dataset['no_of_orders'] = dataset.groupby('product_id')['add_to_cart_order'].transform(sum)
    # dataset=dataset.drop_duplicates('product_id', keep='first', inplace=False)
    # dataset=dataset.drop(['add_to_cart_order'], axis=1)
    # dataset=dataset.sort_values(by='no_of_orders',ascending=False)
    # dataset=dataset.iloc[:20,:]


    # dataset.rename(columns={'product_id': 'product'}, inplace=True)

    # dataset=dataset.join(products_df['product_name'],on='product',rsuffix='_id')
    # dataset=dataset.reset_index(drop=True)

    cc='dataset.to_json()'

 

    # chart = serialize(
    #         df=dataset,
    #         render_to='Leak Values',
           
           
    #         use_index=False,
    #         output_type='json')

    return render(request, "app/DjangoHichartTest.html", context={"chart":cc})

