from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class TodayPageView(TemplateView):
    template_name = "today.html"


class FuturePageView(TemplateView):
    template_name = "future.html"


class PastPageView(TemplateView):
    template_name = "past.html"