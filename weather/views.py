from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import CoordinateForm
from django.urls import reverse_lazy

import requests
from geopy.geocoders import Nominatim


class HomePageView(TemplateView):
    template_name = "home.html"


def get_weather(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CoordinateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CoordinateForm()
    return render(request, "today.html", {"form": form})



class TodayWeatherView(TemplateView):
    template_name = "today.html"


    def weather_create_view(request):
        # if this is a POST request we need to process the form data
        if request.method == "POST":
            # create a form instance and populate it with data from the request:
            form = CoordinateForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect("/thanks/")

        # if a GET (or any other method) we'll create a blank form
        else:
            form = CoordinateForm()
        return render(request, "today.html", {"form": form})

    def find_weather_at_coordinates(latitude, longitude):
        api_url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current_weather=true".format(
            latitude, longitude)
        response = requests.get(api_url)
        return response.json()['current_weather']

    # weather = find_weather_at_coordinates(latitude, longitude)


class FutureWeatherView(TemplateView):
    template_name = "future.html"


class PastWeatherView(TemplateView):
    template_name = "past.html"