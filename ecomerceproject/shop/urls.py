from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [

     path('',views.home, name='home' ),
     path('<slug:category_slug>/', views.allProductCategory, name='allProductCategory'),
     path('<slug:category_slug>/<slug:product_slug>/', views.productDetail, name='productDetail'),
]