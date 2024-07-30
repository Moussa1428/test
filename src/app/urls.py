from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="app-index"),
    path('article_<str:num>/', article, name="app-article_")
]

