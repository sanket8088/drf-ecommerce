from django.urls import path

# from user.views import TestView, SingUpView, LoginView, AddAddressView, PutDeleteAddressView

from products.views import AddCategoriesView, GetProductsView, GetSingleProductView


urlpatterns = [
    path("category", AddCategoriesView.as_view()),
    path("category/<int:category_id>/product", GetProductsView.as_view()),
    path("category/<int:category_id>/product/<int:product_id>", GetSingleProductView.as_view()),
        ]