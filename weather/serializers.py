from rest_framework import serializers 
from . models import *
  
class ReactSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = React 
        fields = ['name', 'detail'] 




class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['city', 'temperature', 'humidity', 'country_code', 'coordinate', 'pressure']

    def validate_temperature(self, value):
        """
        Validate that the temperature is a valid float value.
        """
        try:
            float(value)
        except ValueError:
            raise serializers.ValidationError("Temperature must be a valid number.")
        return value

    def validate_humidity(self, value):
        """
        Validate that the humidity is a valid float value.
        """
        try:
            float(value)
        except ValueError:
            raise serializers.ValidationError("Humidity must be a valid number.")
        return value
