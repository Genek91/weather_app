from django.http import HttpResponse
import requests
from django.shortcuts import render
from weather.forms import CityForm

from app.settings import API_KEY, API_URL


def index(request) -> HttpResponse:
    """Главная страница."""

    form = CityForm(request.POST or None)
    context = {'form': CityForm()}

    if form.is_valid():
        city = form.cleaned_data.get('name')

        response = requests.get(API_URL.format(city, API_KEY))

        if 'locations' in response.text:
            data = response.json()

            context = {
                'form': form,
                'info': {
                    'city': city,
                    'data': data['locations'][city]['values']
                }
            }
        else:
            context = {'form': CityForm(), 'error': 'Город не найден'}

    return render(request, 'weather/index.html', context)
