from django.urls import path
from .apiview import *

app_name = 'blog_api'

urlpatterns = [
    path('list' , ArticleListView.as_view() , name='lists')
]