import uuid
from django.contrib.gis.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField


class Cop(models.Model):

    STATUS_ONLINE = '1'
    STATUS_OFFLINE = '0'

    COP_STATUS = (
        (STATUS_ONLINE, 'Online'),
        (STATUS_OFFLINE, 'Offline')
    )

    cop = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=COP_STATUS, default='0')
    point = models.PointField(null=True, blank=True)
    socket_id = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = "Cop"
        verbose_name_plural = "Cops"

    def __str__(self):
        return self.cop.get_full_name()


class DispatchLog(models.Model):

    citizen = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cop = models.ForeignKey(Cop, on_delete=models.CASCADE)
    location = models.PointField(null=True, blank=True)

    class Meta:
        verbose_name = "Dispatch Log"
        verbose_name_plural = "Dispatch Logs"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("DispatchLog_detail", kwargs={"pk": self.pk})
