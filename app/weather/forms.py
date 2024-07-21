from django import forms


class CityForm(forms.Form):
    """Форма для названий городов."""
    name = forms.CharField(
        max_length=100,
        label='Город'
    )
