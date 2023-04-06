from django.urls import path
from .views import ProductList,ProductDetail

urlpatterns=[
    path("product/",ProductList.as_view(),name="list"),
    path("product/<int:id>/",ProductDetail.as_view(),name="detail"),
]