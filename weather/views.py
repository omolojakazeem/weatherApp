from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm


def index(request):
    template = 'weather/index.html'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=Imperial&appid=289d501a725197d0347d2f21bad60c20'
    err_msg = ''
    message = ''
    message_class = ''
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['city_name']
            city_exist = City.objects.filter(city_name=new_city).count()
            if city_exist == 0:
                req = requests.get(url.format(new_city)).json()
                if req['cod'] == 200:
                    form.save()
                else:
                    err_msg = "City does not exist in the world"
            else:
                err_msg = "City already added in your dashboard"
        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added Successfully'
            message_class = 'is-success'
    form = CityForm()
    print(err_msg)
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        req = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.city_name,
            'temperature': req['main']['temp'],
            'description': req['weather'][0]['description'],
            'icon': req['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    context = {
        'city_weather': weather_data,
        'city_form': form,
        'message': message,
        'message_class': message_class,
    }
    return render(request, template_name=template, context=context)


def delete(request, city_name):
    City.objects.get(city_name=city_name).delete()
    return redirect('dashboard')
