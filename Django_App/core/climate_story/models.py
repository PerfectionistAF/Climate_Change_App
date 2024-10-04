from django.db import models

# Create your models here.
class Emissions(models.Model):
    entity = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()#####for visualization
    year = models.IntegerField()
    electricity_access = models.FloatField()
    cooking_fuel_access = models.FloatField()
    renewable_electricity_capacity = models.FloatField()
    fossil_fuel_electricity = models.FloatField()
    nuclear_electricity = models.FloatField()
    renewable_electricity = models.FloatField()
    low_carbon_electricity = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.entity} id: {self.id}"  ##return a string


