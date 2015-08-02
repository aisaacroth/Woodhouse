#!/usr/bin/env python3.4

from datetime import date
import json

def collect_time_information():
    time = {}
    time['date'] = date.today().strftime('%Y-%m-%d')
    time['tod'] = input("What time of day is it? (e.g., Morning, Afternoon, Evening, Night) ")
    return time


def collect_weather_data():
    weather = {}
    weather['weather'] = input("Please input today's weather conditions (e.g., Cloudy, Sunny, etc..:): ")
    weather['temp-high'] = input("Please input an integer value for today's high temperature (in degrees Fahrenheit): ") 
    weather['temp-low'] = input("Please input an integer value for today's low temperature (in degrees Fahrenheit): ")
    weather['precip'] = input("Please input today's percent chance of preciptation: ")

    return weather


def collect_dress_data():
    dress = {}
    dress['hat'] = hat()
    dress['glass'] = glasses()
    dress['scarf'] = scarf()
    dress['coat'] = coat()
    dress['outer'] = outer_layer()
    dress['inner'] = inner_layer()
    dress['pants'] = pants()
    dress['socks'] = socks()
    dress['shoes'] = shoes()
    return dress


def hat():
    hat = {}
    hat['bool'] = 1 if input("Did you wear a hat? (y/n) ") == 'y' else 0
    hat['type'] = input("What kind of hat did you wear? ") if hat['bool'] else None
    return hat


def glasses():
    glass = {}
    glass['bool'] = 1 if input("Did you wear glasses? (y/n) ") == 'y' else 0
    glass['type'] = input("What type of glasses did you wear? ") if glass['bool'] else None
    return glass


def scarf():
    scarf = {}
    scarf['bool'] = 1 if input("Did you wear a scarf? (y/n) ") == 'y' else 0
    return scarf


def coat():
    coat = {}
    coat['bool'] = 1 if input("Did you wear a coat? (y/n) ") == 'y' else 0
    coat['type'] = input("What kind of hat did you wear? ") if coat['bool'] else None
    return coat


def outer_layer():
    outer = {}
    outer['bool'] = 1 if input("Did you wear an outer layer? (y/n) ") == 'y' else 0
    outer['type'] = input("What kind of outer layer did you wear? ") if outer['bool'] else None
    return outer


def inner_layer():
    inner = {}
    inner['type'] = input("What kind of shirt did you wear? ")
    return inner


def pants():
    pants = {}
    pants['type'] = input("What kind of pants did you wear? ")
    return pants


def socks():
    socks = {}
    socks['bool'] = 1 if input("Did you wear socks? (y/n) ") == 'y' else 0
    socks['type'] = input("What kind of socks did you wear? ") if socks['bool'] else None
    return socks


def shoes():
    shoes = {}
    shoes['type'] = input("What kind of shoes did you wear? ")
    return shoes


def collect_comfort_data():
    comfort = {}
    comfort['val'] = input("On a scale of 1 to 10, how comfortable were your clothes today? ")
    return comfort


def main():
    entries = []

    with open('records.json', mode='r', encoding='utf-8') as weather_file:
        entries = json.load(weather_file)

    data = {}
    
    data['time'] = collect_time_information()
    data['weather'] = collect_weather_data()
    data['dress'] = collect_dress_data()
    data['comfort'] = collect_comfort_data()
    entries.append(data)

    with open('records.json', 'w') as weather_file:
        json.dump(entries, weather_file)


if __name__ == '__main__':
    main()
