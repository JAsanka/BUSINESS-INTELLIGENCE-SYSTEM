from django.conf.urls import url
from app import views
from .DjangoHichart import hichartGenerate
from .DjangoRestApi import ChartData

urlpatterns = [
    url(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    url(r'^home$', views.index, name='index'),
    url(r'^$', views.login, name='login'),

    #charts
    url(r'^highChart$', hichartGenerate, name='login'),
    
    url(r'^api/chart/data$', ChartData.as_view()),
    
    ]