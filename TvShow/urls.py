from django.contrib import admin
from django.urls import path
from . import views

app_name = "TvShow" #Redirect için gerek

urlpatterns = [
    path('crime/', views.crime, name="crime"),
    path('comedy/', views.comedy, name="comedy"),
    path('mystery/', views.mystery, name="mystery"),
    path('scifi/', views.scifi, name="scifi"),
    path('sport/', views.sport, name="sport"),
    path('detail/<int:id>', views.detail, name="detail"), #<-------
    # path('detail/<str:title>', views.detail, name="detail"), #<-------
    path('comment/<int:id>', views.comment, name="comment"),
]