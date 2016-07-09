import requests

def get_weather_forecast():
    # connecting to the weather api
    url = "http://api.openweathermap.org/data/2.5/weather?zip=08540,us&units=imperial&appid=c3a2b88d0195ab9136f72c2270320a91"
    weather_request = requests.get(url)
    weather_json = weather_request.json()
    # print(weather_json)

    # Parsing JSON
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    #Creating forcasting string
    forecast = 'The Circus forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min))

    return forecast

