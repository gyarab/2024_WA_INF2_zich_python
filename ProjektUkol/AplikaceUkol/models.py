from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)  # Manufacturer name
    established = models.PositiveIntegerField()  # Year established
    countryOfOrigin = models.CharField(max_length=255)  # Country of origin
    defunct = models.BooleanField()  # Whether the manufacturer is still active

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Category name

    def __str__(self):
        return self.name

class EngineSpecifications(models.Model):  # Renamed from CarSpecifications
    name = models.CharField(max_length=255)  # Engine name
    engine = models.CharField(max_length=255)  # Engine type
    fuel = models.CharField(max_length=255)  # Fuel type
    displacement = models.FloatField()  # Engine displacement in liters
    power = models.PositiveIntegerField()  # Power in kW
    kilometrageCity = models.FloatField()  # Fuel consumption in city (L/100 km)
    kilometrageRoad = models.FloatField()  # Fuel consumption on road (L/100 km)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)  # Manufacturer of the engine
    categories = models.ManyToManyField('Category')  # Categories associated with the engine

    def __str__(self):
        return self.name

