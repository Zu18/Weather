from django.urls import path
from .views import HomePageView, TodayPageView, FuturePageView, PastPageView

urlpatterns = [
    path('past/', PastPageView.as_view(), name='past'),
    path('future/', FuturePageView.as_view(), name='future'),
    path('today/',  TodayPageView.as_view(), name='today'),
    path('', HomePageView.as_view(), name='home'),
]