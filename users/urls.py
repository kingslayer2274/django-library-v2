from . import views
from django.urls import path

urlpatterns = [
    path('login',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('logout', views.logout, name='logout'),
    path('home',views.homepage,name='homepage')
]