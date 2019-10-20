from django.urls import path
from dispatch.views import CopApiList, NearbyCopApiList
urlpatterns = [
    path("cops", CopApiList.as_view(), name="cops"),
]