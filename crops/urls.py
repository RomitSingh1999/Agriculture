from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.crops, name='crops'),
    path('home', views.crops, name='crops'),
    path('ajax', views.data, name='data'),
    path('feature1', views.feature1, name='feature1'),
    path('feature2', views.feature2, name='feature2'),
    path('show_my_data', views.show, name='show'),

]