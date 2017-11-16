from django.conf.urls import url
from app import views
from .DjangoHichart import hichartGenerate
from .DjangoRestApi import ChartData
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    url(r'^home$', views.index, name='index'),
    
  #temp login
    url(r'^$', auth_views.login, name='login'),
   # url(r'^logout/$', auth_views.logout, name='logout'),
    
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    

    #charts
    url(r'^highChart$', hichartGenerate, name='highchart'),
    
    url(r'^api/chart/data$', ChartData.as_view()),
    
    ]