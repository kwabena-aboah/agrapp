from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='products_index'),
    url(r'^categories/(?P<slug>[\w-]+)/$', CategoryProductsView.as_view(), {'page_num': 1}, name='products_category'),
    url(r'^categories/(?P<slug>[\w-]+)/(?P<page_num>\d+)/$', CategoryProductsView.as_view(), name='products_category'),
    url(r'^manufacturers/(?P<slug>[\w-]+)/$', ManufacturerProductsView.as_view(),
        {'page_num': 1}, name='products_manufacturer'),
    url(r'^manufacturers/(?P<slug>[\w-]+)/(?P<page_num>\d+)/$',
        ManufacturerProductsView.as_view(), name='products_manufacturer'),
    url(r'^search/$', SearchProductsView.as_view(), {'page_num': 1}, name='products_search'),
    url(r'^search/(?P<page_num>\d+)/$', SearchProductsView.as_view(), name='products_search'),
    url(r'^products/(?P<product_id>\d+)/(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='products_product'),
    url(r'^change_currency/$', ChangeCurrencyView.as_view(), name='products_change_currency'),
]