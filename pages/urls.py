
from django.urls import path
from . import views

urlpatterns = [
    path('',views.mainpage),
    path('company/',views.company),
    path('login/',views.login),
    path('signUp/',views.signUp),
    path('myPage/',views.myPage),
]
