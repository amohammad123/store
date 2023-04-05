from django.urls import path
from . import views
from .views import ProductList,ProductDetail

app_name = 'store'

urlpatterns=[
    # path('', views.index, name='index'),
    path("",ProductList.as_view(),name="list"),
    path("<int:pk>",ProductDetail.as_view(),name="detail"),
]