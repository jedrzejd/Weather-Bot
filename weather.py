import discord
from request import get_current_weather_from_city_name

color = 0xFF6500
default_city = 'Białystok'
key_features = {
    'temp': 'temperatura',
    'feels_like': 'temperatura odczuwalna',
    'pressure': 'ciśnienie',
    'humidity': 'wilgotność'
}


def weather_message(location=default_city):
    data = get_current_weather_from_city_name(location)
    message = discord.Embed(
        title=f'Pogoda {location}',
        description=f'Obecna pogoda w mieście {location}.',
        color=color
    )
    for key in key_features:
        message.add_field(
            name=key_features[key],
            value=str(data[key]),
            inline=False
        )
    return message


def error_message(location=default_city):
    message = discord.Embed(
        title='Bład',
        description=f'Brak danych o pogodzie w {location}.',
        color=color
    )
    return message

