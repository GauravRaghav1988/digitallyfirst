
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home_view,name="home"),
    path('blog/',views.blog,name="blog"),
    path('registration/',views.registration,name="registration"),
    path('services/',views.services,name="registration"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('login/', views.loginuser, name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('database/', views.data, name="data"),
    # path('reset/', views.reset, name="resetlogin"), 

#     path('me/', views.me, name="me_page"),
#     path('webdev/', views.webdev, name="webdev"),
#     path('dm/', views.dm, name="dm"),
#     path('weather/', views.weather, name="weather"),
#     path('admin/', views.admin, name="admin"),
]
