##STEP 1: create serializers for api, rest framework
from rest_framework import serializers
from climate_story.models import Emissions

class EmissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emissions
        fields = (   ##cast fields in a tuple
            'id',
            'entity',
            'latitude',
            'longitude',
            'year',
            'electricity_access',
            'cooking_fuel_access',
            'renewable_electricity_capacity',
            'fossil_fuel_electricity',
            'nuclear_electricity',
            'renewable_electricity',
            'low_carbon_electricity',
            'created',
        )  ##optimize this later