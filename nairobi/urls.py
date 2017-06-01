"""nairobi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url 
from django.contrib import admin
from django.views.generic import TemplateView
from mapgis.views import MapGis, nairobi_view, roads_view, rails_view, cameras_view, construct_view, accidents_view
from home.views import TwitterView, constructions, ChartsView
from contact.views import contact

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MapGis.as_view(), name='mapgis'),



    # mapgis url
     url(r'^nairobi.geojson/', nairobi_view, name='county'),
     url(r'^roads.geojson/', roads_view, name='roads'),
     url(r'^rails.geojson/', rails_view, name='railways'),
    url(r'^camera.geojson/', cameras_view, name='camera'),
    url(r'^construct.geojson/', construct_view, name='construct'),
    url(r'^accidents.geojson/', accidents_view, name='accidents'),
     
     url(r'^twitter/', TwitterView.as_view(), name='twitter'),
     url(r'^construction/', 'home.views.constructions', name='construction'),
     url(r'^charts/', ChartsView.as_view(), name='charts'),
    url(r'^contact/$', 'contact.views.contact', name='contact'),
#    
     
]

admin.site.site_header = 'Nairobi Traffic Dashboard  Admin'
