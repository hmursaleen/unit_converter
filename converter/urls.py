from django.urls import path
from .views import LengthConversionView, WeightConversionView, TemperatureConversionView

app_name = 'converter'

urlpatterns = [
    path('length/', LengthConversionView.as_view(), name='length_conversion'),
    path('weight/', WeightConversionView.as_view(), name='weight_conversion'),
    path('temperature/', TemperatureConversionView.as_view(), name='temperature_conversion'),
]
