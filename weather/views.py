from django.http import JsonResponse
import urllib.request
import json

# source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=10816b9c4c19c3ba2c18756d1f542c3a').read()  



from django.shortcuts import render 
from rest_framework.views import APIView 
from . models import *
from rest_framework.response import Response 
from . serializers import *
# Create your views here. 
  
class ReactView(APIView): 
    
    serializer_class = ReactSerializer 
  
    def get(self, request): 
        detail = [ {"name": detail.name,"detail": detail.detail}  
        for detail in React.objects.all()] 
        return Response(detail) 
  
    def post(self, request): 
  
        serializer = ReactSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data) 


# views.py


from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .models import Weather  # Import your Weather model


 



# from rest_framework.views import APIView
# from rest_framework.response import Response
# import requests

# class GetWeather(APIView):
#     def post(self, request):
#         city = request.data.get('city')
#         api_key = '10816b9c4c19c3ba2c18756d1f542c3a'
#         url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
#         try:
#             response = requests.get(url)
#             data = response.json()
#             print(data)
#             if response.status_code == 200:
#                 temperature = data.get('main', {}).get('temp')
#                 humidity = data.get('main', {}).get('humidity')
                
#                 # Check if both temperature and humidity are available
#                 if temperature is not None and humidity is not None:
#                     # Prepare response data
#                     response_data = {
#                         'city': city,
#                         'temperature': temperature,
#                         'humidity': humidity,
#                     }
#                     return Response(response_data)
#                 else:
#                     return Response({'error': 'Temperature or humidity data not found'}, status=400)
#             else:
#                 return Response({'error': data.get('message', 'Failed to fetch weather data')}, status=response.status_code)
#         except Exception as e:
#             return Response({'error': str(e)}, status=500)

class GetWeather(APIView):
    def post(self, request):
        city = request.data.get('city')
        api_key = '10816b9c4c19c3ba2c18756d1f542c3a'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
        try:
            response = requests.get(url)
            data = response.json()
            print(data)
            if response.status_code == 200:
                temperature = data.get('main', {}).get('temp')
                humidity = data.get('main', {}).get('humidity')
                
                if temperature is not None and humidity is not None:
                    # Save weather data to the database
                    Weather.objects.create(city=city, temperature=temperature, humidity=humidity)
                    
                    # Construct response data
                    response_data = {
                        'city': city,
                        'temperature': temperature,
                        'humidity': humidity,
                    }
                    return Response(response_data)
                else:
                    return Response({'error': 'Temperature or humidity data not found'}, status=400)
            else:
                return Response({'error': data.get('message', 'Failed to fetch weather data')}, status=response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
