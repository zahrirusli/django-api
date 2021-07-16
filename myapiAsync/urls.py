from django.conf.urls import url 
from myapiAsync import views 
 
urlpatterns = [ 
    url(r'^apiAsync/products/add$', views.add_product),
    # url(r'^apiSync/products$', views.get_product_list),
    
    # url(r'^apiSync/products/delete$', views.delete_all_product),
    # url(r'^apiSync/products/(?P<pk>[0-9]+)$', views.get_product_detail),
    # url(r'^apiSync/products/update/(?P<pk>[0-9]+)$', views.update_product_detail),
    # url(r'^apiSync/products/delete/(?P<pk>[0-9]+)$', views.delete_product_by_id),
    
 ]