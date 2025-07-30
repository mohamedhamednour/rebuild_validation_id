from django.db import models

# Create your models here.


class MiddelwareRequestID(models.Model):
    request_id = models.CharField(max_length=36, unique=True)
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    status_code = models.IntegerField(default=200)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.request_id} - {self.method} {self.path}"