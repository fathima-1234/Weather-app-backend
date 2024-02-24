from django.urls import path
from . import views
from .views import GetWeather,ReactView


urlpatterns = [
    path('api/get_weather/', GetWeather.as_view(), name='get_weather'),
    path('',ReactView.as_view(), name="something"), 
]
