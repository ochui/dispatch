from django.urls import path
from dispatch.views import CopApiList
urlpatterns = [
    path("cops", CopApiList.as_view(), name="cops"),
]