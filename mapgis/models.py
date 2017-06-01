from __future__ import unicode_literals

from django.db import models

from django.contrib.gis.db import models

class County(models.Model):
	objectid_1 = models.IntegerField()
	county_nam = models.CharField(max_length=50)
	shape_leng = models.FloatField()
	shape_area = models.FloatField()
	nema_regio = models.CharField(max_length=50)  
	eprc_regio = models.CharField(max_length=50)
	eppc_addit = models.CharField(max_length=50)
	highriskma = models.CharField(max_length=5)
	geom = models.MultiPolygonField(srid=21037)

	def __unicode__(self):
		return self.county_nam

# Auto-generated `LayerMapping` dictionary for County model
county_mapping = {
	'objectid_1' : 'OBJECTID_1',
	'county_nam' : 'COUNTY_NAM',
	'shape_leng' : 'Shape_Leng',
	'shape_area' : 'Shape_Area',
	'nema_regio' : 'Nema_REGIO',
	'id' : 'ID',
	'eprc_regio' : 'EPRC_Regio',
	'eppc_addit' : 'EPPC_addit',
	'highriskma' : 'HighriskMa',
	'geom' : 'MULTIPOLYGON',
}

class Roads(models.Model):
	osm_id = models.FloatField()
	name = models.CharField(max_length=48)
	ref = models.CharField(max_length=16)
	type = models.CharField(max_length=16)
	oneway = models.IntegerField()
	bridge = models.IntegerField()
	maxspeed = models.IntegerField()
	geom = models.MultiLineStringField(srid=21037)


	def __unicode__(self):
		return self.name


   

# Auto-generated `LayerMapping` dictionary for Roads model
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


class Rails(models.Model):
    osm_id = models.FloatField()
    name = models.CharField(max_length=48)
    type = models.CharField(max_length=16)
    geom = models.MultiLineStringField(srid=21037)

# Auto-generated `LayerMapping` dictionary for Rails model
rails_mapping = {
    'osm_id' : 'osm_id',
    'name' : 'name',
    'type' : 'type',
    'geom' : 'MULTILINESTRING',
}

class Camera(models.Model):
    name = models.CharField(max_length=254)
    lat = models.FloatField()
    long = models.FloatField()
    geom = models.MultiPointField(srid=4326)
    
    def __unicode__(self):
		return self.name

# Auto-generated `LayerMapping` dictionary for Camera model
camera_mapping = {
    'name' : 'name',
    'lat' : 'lat',
    'long' : 'Long',
    'geom' : 'MULTIPOINT',
}

class Construct(models.Model):
    osm_id = models.FloatField()
    timestamp = models.CharField(max_length=20)
    name = models.CharField(max_length=48)
    type = models.CharField(max_length=16)
    geom = models.MultiPointField(srid=4326)
    
    def __unicode__(self):
		return self.name


# Auto-generated `LayerMapping` dictionary for Construct model
construct_mapping = {
    'osm_id' : 'osm_id',
    'timestamp' : 'timestamp',
    'name' : 'name',
    'type' : 'type',
    'geom' : 'MULTIPOINT',
}


class Accidents(models.Model):
    locations = models.CharField(max_length=80)
    type = models.CharField(max_length=80)
    description = models.CharField(max_length=80)
    time = models.CharField(max_length=80)
    date = models.CharField(max_length=80)
    geom = models.MultiPointField(srid=4326)
    
    def __unicode__(self):
		return self.locations

# Auto-generated `LayerMapping` dictionary for Accidents model
accidents_mapping = {
    'county' : 'county',
    'ward' : 'ward',
    'constituen' : 'constituen',
    'name' : 'name',
    'geom' : 'MULTIPOINT',
}





