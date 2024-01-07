from django.urls import path
from . import views

urlpatterns = [ 
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('welcome/', views.welcome_view, name='welcome'),
    ]