from django.contrib import admin
from django.contrib.gis import admin

from .models import  County, Roads, Rails, Camera, Construct, Accidents

# Register your models here.

admin.site.register(County, admin.OSMGeoAdmin)
admin.site.register(Roads, admin.OSMGeoAdmin)
admin.site.register(Rails, admin.OSMGeoAdmin)
admin.site.register(Camera, admin.OSMGeoAdmin)
admin.site.register(Construct, admin.OSMGeoAdmin)
admin.site.register(Accidents, admin.OSMGeoAdmin)