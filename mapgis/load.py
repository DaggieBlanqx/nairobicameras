import os
from django.contrib.gis.utils import LayerMapping
from .models import Roads

roads_mapping = {
	'osm_id' : 'osm_id',
	'name' : 'name',
	'ref' : 'ref',
	'type' : 'type',
	'oneway' : 'oneway',
	'bridge' : 'bridge',
	'maxspeed' : 'maxspeed',
	'geom' : 'MULTILINESTRING',
}




accidents_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../mapgis/data/Roads.shp'))

def run(verbose=True):
    lm = LayerMapping(Roads, accidents_shp ,roads_mapping, transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)