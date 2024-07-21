from django.shortcuts import render
import requests
from weather.forms import CityForm
from app.settings import API_KEY, API_URL


def index(request):
    """Главная страница."""

    form = CityForm(request.POST or None)
    context = {'form': CityForm()}

    if form.is_valid():
        city = form.cleaned_data.get('name')

        res = requests.get(API_URL.format(city, API_KEY))

        if 'locations' in res.text:
            data = res.json()

            context = {
                'form': form,
                'info': {
                    'city': city,
                    'data': data['locations'][city]['values']
                }
            }

    return render(request, 'weather/index.html', context)
