from django.urls import path
from .views import HomePageView, TodayWeatherView, FutureWeatherView, PastWeatherView

urlpatterns = [
    path('past/', PastWeatherView.as_view(), name='past'),
    path('future/', FutureWeatherView.as_view(), name='future'),
    path('today/', TodayWeatherView.as_view(), name='today'),
    path('', HomePageView.as_view(), name='home'),
]