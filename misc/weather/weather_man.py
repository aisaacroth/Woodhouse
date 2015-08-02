#!/usr/bin/env python3

import json
import os
import urllib.request

class WeatherMan:
    UWS_LAT = "40.81060946175836"
    UWS_LON = "-73.95205999207417"
    FCST_TYPE = "json"

    def __init__(self):
        self.current_weather = {}
        self.forecast = []
        self.location = 'Morningside Heights, New York, New York'

    def retrieve_weather_info(self):
        response = urllib.request.urlopen('http://forecast.weather.gov/MapClick'
            '.php?lat={0}&lon={1}&FcstType={2}'.format(WeatherMan.UWS_LAT,
                WeatherMan.UWS_LON,
                WeatherMan.FCST_TYPE))
        return response

    def write_response_to_file(self, response):
        json_file = open('weather.json', 'wb')
        json_file.write(response.read())
        json_file.close()

    def load_json_file(self, filename):
        with open(filename) as json_file:
            json_data = json.load(json_file)
        return json_data

    def get_times(self, json_data):
        self.forecast = [ {'time': time} for time in json_data['time']['startPeriodName']]

    def fill_out_forecast(self, json_data):
        forecast_data = json_data['data']
        for i in range(len(self.forecast)):
            self.forecast[i]['temp'] = forecast_data['temperature'][i]
            self.forecast[i]['percent'] = forecast_data['pop'][i]
            self.forecast[i]['weather'] = forecast_data['weather'][i]
            self.forecast[i]['text'] = forecast_data['text'][i]
            self.forecast[i]['label'] = json_data['time']['tempLabel'][i]

    def fill_out_current_forecast(self, json_data):
        current = json_data['currentobservation']

        self.current_weather['locale'] = current['name']
        self.current_weather['temp'] = current['Temp']
        self.current_weather['weather'] = current['Weather']

    def tell_current_weather(self):
        os.system("say 'Currently, from "
            "{}'".format(self.current_weather['locale']))
        os.system("say 'The temperature is {} degrees "
            "Fahrenheit'".format(self.current_weather['temp']))
        os.system("say '{}'".format(self.current_weather['weather']))

    def tell_five_day_forecast(self):
        os.system("say 'And now for the 5 day forecast'")
        os.system("say 'From {}'".format(self.location))

        for day in self.forecast[:-3]:
            os.system('say {}'.format(day['time']))
            os.system('say {}'.format(day['text']))

    def tell_seven_day_forecast(self):
        os.system("say 'And now for the 7 day forecast'")
        os.system("say 'From {}'".format(self.location))

        for day in self.forecast:
            os.system('say {}'.format(day['time']))
            os.system('say {}'.format(day['text']))
            

def main():
    woodhouse = WeatherMan()
    response = woodhouse.retrieve_weather_info()
    woodhouse.write_response_to_file(response)
    json_data = woodhouse.load_json_file('weather.json')
    woodhouse.get_times(json_data)
    woodhouse.fill_out_forecast(json_data)
    woodhouse.fill_out_current_forecast(json_data)
    woodhouse.tell_current_weather()
    woodhouse.tell_seven_day_forecast()


main()
