from http import HTTPStatus

from django.http import HttpResponse
import requests
from django.shortcuts import render
from weather.forms import CityForm

from app.settings import API_KEY, API_URL


def index(request) -> HttpResponse:
    """Главная страница."""

    form = CityForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        city = form.cleaned_data.get('name')

        response = requests.get(API_URL.format(city, API_KEY))

        if response.status_code == HTTPStatus.OK:
            data = response.json()

            context['info'] = {
                'city': city,
                'data': data['locations'][city]['values']
            }
        else:
            form.add_error(None, 'Ошибка при запросе к API')

    return render(request, 'weather/index.html', context)
