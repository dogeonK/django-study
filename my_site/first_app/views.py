from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

articles = {
    'sports' : 'Sports Page',
    'finance' : 'Finance Page',
    'politics' : 'Politics Page',
}

# Create your views here.
def simple_view(request):
    return HttpResponse("Simple View")

def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        result = 'No page for that topic!'
        raise Http404("404 GENERIC ERROR")
        # return HttpResponseNotFound(result)

def num_page_view(request, num_page):
    
    topics_list = list(articles.keys())
    topic = topics_list[num_page]

    # return HttpResponseRedirect(topic)
    return HttpResponseRedirect(reverse('topic-page', args=[topic]))