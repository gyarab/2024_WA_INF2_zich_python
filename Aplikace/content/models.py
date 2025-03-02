from django.db import models

class Engine(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    horsepower = models.IntegerField()
    torque = models.IntegerField()
    displacement = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name