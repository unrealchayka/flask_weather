import requests


def weather(city):
    appid = 'e7e20ee0282592cb47398eecefe93435'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=' + appid
    res = requests.get(url).json()
    city_info = {
        'city' : city,
        'temp' : res['main']['temp'],
        'icon' : res['weather'][0]['icon'],
    }
    return city_info