

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse



def index(request):
    context = {}
    template = loader.get_template('app/index3.html')
    return HttpResponse(template.render(context, request))



def charts(request):
    context = {}
    template = loader.get_template('app/charts.html')
    return HttpResponse(template.render(context, request))

def predictions(request):
    context = {}
    template = loader.get_template('app/predictions.html')
    return HttpResponse(template.render(context, request))





# def login(request):
#     context = {}
#     template = loader.get_template('app/login.html')
#    # return HttpResponse(template.render(context, request))
#     return render(request,"app/login.html",{})


def allHtml(request):
    context = {}
   
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))
