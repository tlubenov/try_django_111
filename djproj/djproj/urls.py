"""djproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from restaurants.views import HomeView, AboutView, ContactView, MapView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),

    url(r'^items/', include('menus.urls', namespace='menus')),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),

    # hard coded URIs
#    url(r'^restaurants/mexican/$', MexicanRestaurantListView.as_view()),
#    url(r'^restaurants/asian/$', AsianFusionRestaurantListView.as_view()),

    # flexible url query sets
#    url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),

    # here uuid can be used
#    url(r'^restaurants/(?P<rest_id>\w+)/$', RestaurantDetailView.as_view()),



#    url(r'^restaurants/$', RestaurantListView.as_view(), name='restaurants'),
#    url(r'^restaurants/create/$', RestaurantCreateView.as_view()),
#    # URI with slug field
#    url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='restaurant-details'),


    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),#AboutView.as_view()),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^contact/(?P<id>\d+)/$', MapView.as_view(), name='contact123'),
]
