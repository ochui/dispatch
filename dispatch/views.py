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

    def get_queryset(self):
        return Cop.objects.all()



class NearbyCopApiList(ListAPIView):
    serializer_class = CopSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cop.objects.annotate(
            distance=Distance(
                'location', fromstr(
                    f'POINT({self.kwargs["longitude"]} {self.kwargs["latitude"]})', srid=4326)
            )
        ).order_by('distance')[0:10]
