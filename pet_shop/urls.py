from django.contrib import admin
from django.urls import path
from APP.views import *
from django.conf.urls.static import static
from pet_shop.settings import STATIC_ROOT, STATIC_URL



     
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('products/', products_view, name = 'product'),
    #path('products/<int:id>/', product_view, name = 'product'),
    #path('products/categories/parrot/', default),
    #path('products/categories/dog/', default2),
    #path('products/categories/cat/', default3),
    #path('list/', Product.hello),
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('products/cat1/', cat1),
    path('products/cat2/', cat2),
    path('products/dog1/', dog1),
    path('products/dog2/', dog2),
    path('products/parrot1/', parrot1),
    path('products/parrot2/', parrot2),
    path('products/buy/', buy),
    path('products/thanks/', thanks, name='thanks'),
    path('products/drakon1/', friend),
    path('products/fish1/', fish1),
    path('products/dog3/', dog3),
    path('products/drakon2/', drakon2),
    path('products/parrot3/', parrot3),
]

urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT )