from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView

from django.http import HttpResponse, HttpResponseRedirect
from mapgis.models import  Construct, Accidents
from django.template import RequestContext
from highcharts.views import HighChartsBarView

# Create your views here.

class TwitterView(TemplateView):
	template_name = "twitter.html"

def constructions(request):
	construction = Construct.objects.all()
	accidents = Accidents.objects.all()
	

	return render(request,'tables.html', {'construction': construction, 'accidents':accidents})

class ChartsView(TemplateView):
	template_name = "charts.html"

class BarView(HighChartsBarView):	
	categories = ['Orange', 'Bananas', 'Apples']
	
	@property
	def series(self):
		result = []
		for name in ('Joe', 'Jack', 'William', 'Averell'):
			data = []
			for x in range(len(self.categories)):
				data.append(random.randint(0, 10))
			result.append({'name': name, "data": data})
		return result

	