from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('authorize', views.authorize, name='authorize'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name="signup"),
    path('lumberapplication', views.lumberapplication, name="lumberapplication"),
    path('qr/<int:id>', views.qr, name="qr"),
    path('profile', views.profile, name="profile"), 
    path('forgot', views.forgot, name="forgot")
]