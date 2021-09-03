
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cocktail,name='cocktail'),
    path('cocktail_details/<int:id>/',views.cocktail_detail, name="cocktail-detail"),

]