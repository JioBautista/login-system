from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductsList.as_view()),
    path("products/<int:pk>/", views.ProductDetail.as_view()),
]
