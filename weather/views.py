from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class TodayWeatherView(TemplateView):
    template_name = "today.html"


class FutureWeatherView(TemplateView):
    template_name = "future.html"


class PastWeatherView(TemplateView):
    template_name = "past.html"