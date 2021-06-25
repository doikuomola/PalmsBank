from django.urls import path

from . import views

app_name = 'banking'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    
]