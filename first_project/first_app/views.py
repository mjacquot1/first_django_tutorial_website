from django.shortcuts import render
from django.http.response import (
    HttpResponse, # An http response object
    Http404, # http 404
    HttpResponseRedirect, # http redirect ability
    )
from django.urls import (
    reverse, # Allow for reverse lookups from path names
)

# Create your views here.

def simple_view(request):
    return render(request, 'first_app/example.html')

# # Each view requires a function
# # Each view must return an http response object.
# def index(request): #Call it "request" as convention
#     return HttpResponse("Hello World")

# def simple_view(request):
#     return HttpResponse("SIMPLE VIEW")


# # Dynamic views
# articles = {
#     'sports':'Sports View',
#     'finance':'Finance View',
#     'politics':'Politics Page'
# }

# def news_view(request, topic):
#     print('HEYYYYYY:', topic)
#     try:
#         result = articles[topic]
#         return HttpResponse(result)
#     except:
#         result = 'No page for that topic!'
#         raise Http404('404 GENERIC ERROR') 

# # Redirect views
# def num_page_views(request, num_page):
#     topics_list = list(articles.keys())
#     topic = topics_list[num_page]

#     print('WHYYYYYYYYYY:', topic)
    
#     return HttpResponseRedirect(reverse('topic-page', args=[topic])) # Find URL path called 'topic-page' and send it 'topic' value