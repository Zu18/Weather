from django.urls import path
from .views import HomePageView, TodayWeatherView, FutureWeatherView, PastWeatherView, get_weather

urlpatterns = [
    path('past/', PastWeatherView.as_view(), name='past'),
    path('future/', FutureWeatherView.as_view(), name='future'),
    path('today/', get_weather, name='today'),
    path('', HomePageView.as_view(), name='home'),
]