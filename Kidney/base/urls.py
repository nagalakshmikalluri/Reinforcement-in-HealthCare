from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('index/', views.index, name='index'),
    path('signup/',views.SignupPage,name='signup'),
    path('result/', views.result, name='result'),
]