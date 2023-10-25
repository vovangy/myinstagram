from django.db import models
from moment.models import Moment

class Tag(models.Model):
    title = models.CharField(max_length=50)
    moment_id = models.ForeignKey(Moment, on_delete=models.CASCADE)