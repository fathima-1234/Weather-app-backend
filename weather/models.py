from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    
    country_code = models.CharField(max_length=100, default='US')
    coordinate = models.CharField(max_length=100, default="(0.0, 0.0)")  # Default coordinates
    pressure = models.CharField(max_length=100, default='0')




  

  
  
class React(models.Model): 
    name = models.CharField(max_length=30) 
    detail = models.CharField(max_length=500)
