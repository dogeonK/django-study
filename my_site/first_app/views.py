from django.shortcuts import render
from django.http import HttpResponse

articles = {
    'sports' : 'Sports Page',
    'finance' : 'Finance Page',
    'politics' : 'Politics Page',
}

# Create your views here.
def simple_view(request):
    return HttpResponse("Simple View")

def news_view(request, topic):
    return HttpResponse(articles[topic])