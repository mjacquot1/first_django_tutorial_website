from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.simple_view) # domain.com/first_app

    # path('', views.index, name='index'),
    # path('simpleview/', views.simple_view, name='simple-view'),
    # # Redirect Routing
    # path('<int:num_page>/', views.num_page_views, name='num-page'),
    # # Dynamic Routing
    # path('<str:topic>/', views.news_view, name='topic-page'), # whatever in the url is passed after 'firstapp/' will be passed through the STRING 'topic'

]