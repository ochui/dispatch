from rest_framework.generics import ListAPIView 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from dispatch.models import Cop
from dispatch.serializers import CopSerializer
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from rest_framework_gis.filters import DistanceToPointFilter
from django.contrib.gis.geos import fromstr

class CopApiList(ListAPIView):

    serializer_class = CopSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    distance_filter_field = 'point'
    filter_backends = (DistanceToPointFilter, )
    bbox_filter_include_overlapping = True # Optional

    def get_queryset(self):
        return Cop.objects.all()



class NearbyCopApiList(ListAPIView):

    serializer_class = CopSerializer
    queryset = Cop.objects.all()
    distance_filter_field = 'geometry'
    filter_backends = (DistanceToPointFilter, )
    bbox_filter_include_overlapping = True # Optional