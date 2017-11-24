from django.shortcuts import render,render_to_response
from django.template import loader
#from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
import numpy as np
# from sklearn.svm import SVR
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score


class Recommendations(APIView):

    authentication_classes = []
    permission_classes = []




    def get(self, request, format=None):

        # df = pd.read_csv("app/pridictingModel/correlation.csv", index_col=0)
        # cor_ = df.corr()

            if(request.method=='POST'):
                def correlations(request):
            
                    # corr=request.POST['CorrInput']

                    # context = {}
                    # template = loader.get_template('app/predict.html')
                    # return HttpResponse(template.render(context, request))

                    # df = pd.read_csv("app/pridictingModel/correlation.csv", index_col=0)
                    # cor_ = df.corr()

                    # def corr_items(item):
                    #     list_item = cor_[item].sort_values(ascending=False).head(10)
                    #     x=list_item.index
                    #     y=list_item.values
                        
                        # plt.figure(figsize=(12,8))
                        # sns.barplot(x,y)
                        # plt.title("Correlated Items", fontsize=30)
                        # plt.xlabel("Items", fontsize=20)
                        # plt.ylabel("Percentage of correlate", fontsize=20)
                        # plt.xticks(rotation="vertical")
                        # plt.show()
                    return (x,y)



                    item = "FIRE POLISHED GLASS NECKL GOLD"
                    X,Y=corr_items(item)
                    print('Searched one')
                    print('Not searched One')                       
                    data={
                            "Items":'Xxxx',"Correlation":'Yxxxx',
                        }

                return Response(data)

            else :

                def corr_items(item):
                    # list_item = cor_[item].sort_values(ascending=False).head(10)
                    # x=list_item.index
                    # y=list_item.values

                    x=1
                    y=1
                    
                    # plt.figure(figsize=(12,8))
                    # sns.barplot(x,y)
                    # plt.title("Correlated Items", fontsize=30)
                    # plt.xlabel("Items", fontsize=20)
                    # plt.ylabel("Percentage of correlate", fontsize=20)
                    # plt.xticks(rotation="vertical")
                    # plt.show()

                return (x,y)

                item = "FIRE POLISHED GLASS NECKL GOLD"
                X,Y=corr_items(item)
                print(X)
                print(Y)

                data={
                        "Items":X,"Correlation":Y,
                    }
                    
                data={
                        "Items":X,"Correlation":Y,
                    }

                return Response(data)
