from django.contrib.auth.models import User
from django.db import models


class LogData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    request_method = models.CharField(max_length=10, verbose_name="Request method", null=True, blank=True,)
    request_body = models.TextField(verbose_name="Request body", null=True, blank=True)
    request_path = models.CharField(max_length=255, verbose_name="Request path", null=True, blank=True, )
    date_time = models.DateTimeField(auto_now_add=True, verbose_name="Date time")

    def __str__(self):
        return str(self.user) + ' ' + str(self.request_path) + ' ' + str(self.date_time)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'
