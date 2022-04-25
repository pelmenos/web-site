from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='main'),

    path('cats', views.ListKittens.as_view(), name='cat'),
    path('dogs', views.ListPupies.as_view(), name='dog'),
    path('about', views.TeamList.as_view(), name='about'),
    path('questions', views.OftenQuest, name='quest'),

    path('cats/<int:pk>/', views.DetailKit.as_view(), name='cat_list'),
    path('dogs/<int:pk>/', views.DetailPup.as_view(), name='dog_list'),

    path('addcat', views.AddCat, name='addcat'),
    path('adddog', views.AddDog, name='adddog'),

]
