from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('login', views.signin, name='signin'),
    path('logout', views.signout, name='signout'),
    path('pricing', views.pricing, name='pricing'),
    path('contact', views.contact, name='contact'),
]