from django.contrib import admin
from django.urls import path
from camu import views

urlpatterns = [
     path("",views.index, name = 'camu')

]