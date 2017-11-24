from django.conf.urls import url
from app import views
from .DjangoHichart import hichartGenerate
from .DjangoRestApi import ChartData
from .Charts.items_sold import itemsSoldData
from .Charts.sales_of_year import SalesOfYearData
from .Charts.monthly_sales import SalesOfMonthData
from .Charts.year_total_Profits_income import SalesProfitOfYearData
from .Charts.frequent_customers import FrequentCustomers
from .Charts.most_profitable_Products import most_profitable_Products
from .Charts.User_logins import loginDeviceData
from .Charts.indexData import indexloadData
from .Charts.CustomersVSno_of_items import CustomersVSno_of_items
from .pridictingModel.Recommandations import Recommendations


from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^.*\.html', views.allHtml, name='All htmls'),


    # The home page
    url(r'^home$', views.index, name='index'),

    url(r'^contactus$', views.contactus, name='index'),
    
    url(r'^aboutus$', views.aboutus, name='aboutus'),
    
    
  #temp login
    url(r'^$', auth_views.login, name='login'),
   # url(r'^logout/$', auth_views.logout, name='logout'),
    
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    

    #charts
    url(r'^Analytics$',views.charts, name='charts'),
    url(r'^temp$',views.charts1, name='charts'),
    url(r'^predictions$',views.predictions, name='predictions'),
    
    url(r'^highChart$', hichartGenerate, name='highchart'),
    
    url(r'^api/chart/data$', ChartData.as_view()),
    url(r'^api/items_sold/data$', itemsSoldData.as_view()),
    url(r'^api/sales_of_year/data$', SalesOfYearData.as_view()),
    url(r'^api/SalesOfMonth/data$', SalesOfMonthData.as_view()),
    url(r'^api/totalSalesProfit/data$', SalesProfitOfYearData.as_view()),
    url(r'^api/FrequentCustomers/data$', FrequentCustomers.as_view()),
    url(r'^api/most_profitable_Products/data$', most_profitable_Products.as_view()),
    url(r'^api/loginDeviceData/data$', loginDeviceData.as_view()), 
    url(r'^api/indexloadData/data$', indexloadData.as_view()),  
    url(r'^api/correlations/data$', Recommendations.as_view()), 
    url(r'^api/CustomersVSno_of_items/data$', CustomersVSno_of_items.as_view()), 
     



    url(r'^api/correlationSearch/data$', Recommendations.as_view(),name='corrdata'), 
    ]


    