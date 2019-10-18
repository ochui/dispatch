from rest_framework.serializers import ModelSerializer, ReadOnlyField
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from dispatch.models import Cop


class CopSerializer(GeoFeatureModelSerializer):
    cop = ReadOnlyField(source='cop.get_full_name')

    class Meta:
        model = Cop
        geo_field = "point"
        fields = (
            'id', 'cop', 'status', 'socket_id',
        )

        read_only_fields = (
            'status',
        )
