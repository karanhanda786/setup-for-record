from django.contrib import admin
from django.urls import path
from expires import views
from django.conf.urls import url, include

app_name = "expires"

urlpatterns = [
    url(r'^create/$', views.ProductCreate.as_view(), name="createProduct"),
    url(r'^allList/$', views.ProductDetail, name="detailProduct"),
    url(r'^Find-any-product-info/$', views.ProductFind, name="findProduct"),

]
