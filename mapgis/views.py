from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import County, Roads, Rails, Camera, Construct, Accidents
# Create your views here.

class MapGis(TemplateView):
	template_name = "map.html" 

def nairobi_view(request):
    nairobi_as_geojson = serialize('geojson', County.objects.all())
    return HttpResponse(nairobi_as_geojson, content_type='json')

def roads_view(request):
    roads_as_geojson = serialize('geojson', Roads.objects.all())
    return HttpResponse(roads_as_geojson, content_type='json')	

def rails_view(request):
    rails_as_geojson = serialize('geojson', Rails.objects.all())
    return HttpResponse(rails_as_geojson, content_type='json')

def cameras_view(request):
    camera_as_geojson = serialize('geojson', Camera.objects.all())
    return HttpResponse(camera_as_geojson, content_type='json')

def construct_view(request):
    construct_as_geojson = serialize('geojson', Construct.objects.all())
    return HttpResponse(construct_as_geojson, content_type='json')

def accidents_view(request):
    accidents_as_geojson = serialize('geojson', Accidents.objects.all())
    return HttpResponse(accidents_as_geojson, content_type='json')




    	