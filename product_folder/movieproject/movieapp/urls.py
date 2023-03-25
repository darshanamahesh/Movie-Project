from . import views
from django.urls import path

app_name='movieapp'
urlpatterns = [

    path('', views.index, name="index"),
    path('movie/<int:movieid>/', views.detail, name="detail"),
    path('add/', views.add_movie, name="add_movie"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),

]