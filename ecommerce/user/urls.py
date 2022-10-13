from django.urls import path

from user.views import TestView, SingUpView


urlpatterns = [
    path("test", TestView.as_view()),
    path("signup",SingUpView.as_view() )
        ]