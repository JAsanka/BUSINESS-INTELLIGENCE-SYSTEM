from django.shortcuts import render,render_to_response
from django.template import loader
from django.http import JsonResponse
#from django.views.generic views

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()


pd.options.mode.chained_assignment = None  # default='warn'

#from subprocess import check_output
#print(check_output(["ls", "../input"]).decode("utf8"))


order_products_train_df = pd.read_csv("app/input/order_products__train.csv")
order_products_prior_df = pd.read_csv("app/input/order_products__prior.csv")
orders_df = pd.read_csv("app/input/orders.csv")
products_df = pd.read_csv("app/input/products.csv")
aisles_df = pd.read_csv("app/input/aisles.csv")
departments_df = pd.read_csv("app/input/departments.csv")


'''What type of products customer purchase most often? '''

def mostOftenPurchases(request,*args,**kwargs):


    dataset = order_products_prior_df.iloc[:,1:3]
    dataset['no_of_orders'] = dataset.groupby('product_id')['add_to_cart_order'].transform(sum)
    dataset=dataset.drop_duplicates('product_id', keep='first', inplace=False)
    dataset=dataset.drop(['add_to_cart_order'], axis=1)
    dataset=dataset.sort_values(by='no_of_orders',ascending=False)
    dataset=dataset.iloc[:20,:]


    dataset.rename(columns={'product_id': 'product'}, inplace=True)

    dataset=dataset.join(products_df['product_name'],on='product',rsuffix='_id').set_index('product')

    # Data to plot
    labels = dataset.iloc[:5,1]
    sizes = dataset.iloc[:5,0]
    
    send = dict(zip(dataset.product_name, dataset.no_of_orders))
    data={
        "sales":10,"customers":'Asanka',
        }

    return JsonResponse(data) 

    