from django.urls import path

# from user.views import TestView, SingUpView, LoginView, AddAddressView, PutDeleteAddressView

from products.views import AddCategoriesView


urlpatterns = [
    path("category", AddCategoriesView.as_view()),
        ]