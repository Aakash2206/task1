from django.conf.urls import url

from filter1 import views

app_name = 'filter1'

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^category/$', views.category, name='category'),
    #url(r'^f1/$', views.f1, name='f1'),
    #url(r'^f2/$', views.f2, name='f2'),
    #url(r'^fs21/$', views.f1, name='fs21'),
    #url(r'^fs22/$', views.f2, name='fs22'),

]
