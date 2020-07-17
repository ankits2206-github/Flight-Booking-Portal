from django.shortcuts import render
from newsapi import NewsApiClient
from .models import *
import requests

# Create your views here.
def newsfun(request):

    if request.method=='POST':
        con=request.POST['country']
        url = 'http://newsapi.org/v2/top-headlines?country='+con+'&apiKey=yourapikey'
        response = requests.get(url)
        top = response.json()

        l=top['articles']
        news.objects.all().delete()
        for i in range(len(l)):
            f = l[i]
            nws=(f['title'])
            desc=(f['description'])
            img=(f['urlToImage'])
            p=news(title = nws,description = desc,image=img)
            p.save()

        cont = country.objects.get(code=con)
        f = country.objects.all()

        context = {'mylist': news.objects.all(), 'country': cont.name, 'con': f}

        return render(request,'newsapp/index.html',context)

    else :
        con = 'in'
        url = 'http://newsapi.org/v2/top-headlines?country=' + con + '&apiKey=6650b13bf8c34555ab296b463ff81d06'
        response = requests.get(url)
        top = response.json()

        l = top['articles']
        news.objects.all().delete()
        for i in range(len(l)):
            f = l[i]
            nws = (f['title'])
            desc = (f['description'])
            img = (f['urlToImage'])
            p = news(title=nws, description=desc, image=img)
            p.save()

        cont=country.objects.get(code=con)
        f=country.objects.all()

        context = {'mylist': news.objects.all(), 'country': cont.name,'con':f}

        return render(request,'newsapp/index.html',context)





