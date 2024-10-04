##STEP 1: create serializers for api, rest framework, suitable format
from rest_framework import serializers
from ..models import Emissions

class DecimalSerializer(serializers.Field):
    def round_hundredth(self, obj):
        return round(obj, 2)
    
    def to_internal_value(self, data):
        return data
    
class EmissionsSerializer(serializers.ModelSerializer):
    created = serializers.SerializerMethodField()  ##need a mthd outside of Meta class to getthe field
    #latitude = round('latitude', 2)
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

    def get_created(self, obj):  ##created date object
        return obj.created.strftime("%Y-%m-%d , %H:%M:%S")