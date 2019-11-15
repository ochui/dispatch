from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws', consumers.CopConsumer),
    path('ws/<socket_id>', consumers.CopConsumer),
]