from django.urls import path

from user.views import TestView, SingUpView, LoginView, AddAddressView, PutDeleteAddressView


urlpatterns = [
    path("test", TestView.as_view()),
    path("signup",SingUpView.as_view() ),
    path("login",LoginView.as_view() ),
    path("address",AddAddressView.as_view() ),
    path("address/<int:address_id>",PutDeleteAddressView.as_view() ),
        ]