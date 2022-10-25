from django.urls import path

from order.views import AddItemToCart


urlpatterns = [
    path("", AddItemToCart.as_view()),
        ]