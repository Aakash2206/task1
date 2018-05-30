from django.conf.urls import url
from django_filters.views import FilterView

from filter2 import views
from filter2.filters import ProductFilter

urlpatterns = [
    # url(r'^$', views.search, name='search'),
    url(r'^$', FilterView.as_view(filterset_class=ProductFilter,
                                  template_name='filter2/product_list.html'), name='search'),
]
