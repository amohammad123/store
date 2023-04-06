from django.urls import path
from . import views
from .views import ProductList,ProductDetail

app_name = 'store'

urlpatterns=[
    path("product/",ProductList.as_view(),name="list"),
    path("product/<int:id>/",ProductDetail.as_view(),name="detail"),
]