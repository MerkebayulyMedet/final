from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name = 'index'),
    path('courses', views.courses, name = 'courses'),
    path('courses/lists', views.lists, name = 'lists'),
    path('courses/lists/article', views.article, name = 'article'),
]
