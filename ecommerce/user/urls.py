from django.urls import path

from user.views import TestView, SingUpView, LoginView


urlpatterns = [
    path("test", TestView.as_view()),
    path("signup",SingUpView.as_view() ),
    path("login",LoginView.as_view() )
        ]