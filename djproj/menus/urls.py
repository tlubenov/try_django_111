from django.conf.urls import url

from .views import (
    ItemCreateView,
    ItemListView,
    ItemUpdateView,
    ItemDetailView,
)


urlpatterns = [
    url(r'^$', ItemListView.as_view(), name='list'),
    url(r'^create/$', ItemCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='detail'),
]
