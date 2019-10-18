from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from dispatch.models import Cop, DispatchLog


@admin.register(Cop)
class CopAdmin(OSMGeoAdmin):

    list_display = ['cop', 'status', 'point']
    

@admin.register(DispatchLog)
class DisPatchLogAdmin(OSMGeoAdmin):
    
    list_display = ['citizen', 'cop', 'location']
