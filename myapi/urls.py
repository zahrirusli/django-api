from django.conf.urls import url 
from myapi import views 
 
urlpatterns = [ 
    url(r'^api/products$', views.get_product_list),
    url(r'^api/products/add$', views.add_product),
    url(r'^api/products/delete$', views.delete_all_product),
    url(r'^api/products/(?P<pk>[0-9]+)$', views.get_product_detail),
    url(r'^api/products/update/(?P<pk>[0-9]+)$', views.update_product_detail),
    url(r'^api/products/delete/(?P<pk>[0-9]+)$', views.delete_product_by_id),
    
 ]