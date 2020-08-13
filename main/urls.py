from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    #path('explore/', views.explore, name='explore'),#we need to create new app for explore
    #path('setProgram', views.setProgram, name='setProgram'),
    #path('setDiet', views.setDiet, name='setDiet'),
]