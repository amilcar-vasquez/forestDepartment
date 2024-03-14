from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/<int:id>', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name="signup"),
    path('application', views.application, name="application"),
    path('qr/<int:id>', views.qr, name="qr"),
    path('profile', views.profile, name="profile"), 
    path('forgot', views.forgot, name="forgot")
]