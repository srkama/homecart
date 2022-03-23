from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import signup

urlpatterns = [
    path('signup', signup),
    path('logout', LogoutView.as_view()),
    path('login', LoginView.as_view())
]
