from django.db import models

# Create your models here.
class React(models.Model):
    model = models.CharField(max_length=20)
    accuracy = models.FloatField()
    cost_in = models.FloatField()
    cost_out = models.FloatField()
    latency = models.FloatField()