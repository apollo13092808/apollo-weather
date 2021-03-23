# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request

from django.shortcuts import render


# Create your views here.
def index(request):
    try:
        if request.method == 'POST':
            city = request.POST['city']

            # source contain JSON data from API
            source = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=48a90ac42caa09f90dcaeee4096b9e53').read()

            # converting JSON data to a dictionary
            list_of_data = json.loads(source)

            # data for variable list_of_data
            country_code = str(list_of_data['sys']['country'])
            coordinate = '(' + str(list_of_data['coord']['lon']) + ' , ' + str(list_of_data['coord']['lat']) + ')'

            temp = list_of_data['main']['temp'] - 273.15
            rounded_temp = round(temp, 2)
            final_temp = str(rounded_temp) + ' ºC'

            pressure = str(list_of_data['main']['pressure'])
            humidity = str(list_of_data['main']['humidity'])
            city_name = str(list_of_data['name'])
            desc = str(list_of_data['weather'][0]['description'])

            data = {
                'country_code': country_code,
                'coordinate': coordinate,
                'temp': final_temp,
                'pressure': pressure,
                'humidity': humidity,
                'city_name': city_name,
                'desc': desc,
            }
            print(data)
        else:
            data = {}
    except:
        data = {
            'country_code': 'Unavailable',
            'coordinate': 'Unavailable',
            'temp': 'Unavailable',
            'pressure': 'Unavailable',
            'humidity': 'Unavailable',
            'city_name': 'Invalid City! Try Again',
            'desc': 'Unavailable',
        }
    return render(request, 'main/index.html', data)
