import discord
from request import get_current_weather_from_city_name

color = 0xFF6500
default_city = 'Białystok'
key_features = {
    'temp': 'Temperatura',
    'feels_like': 'Temperatura odczuwalna',
    'pressure': 'Ciśnienie',
    'humidity': 'Wilgotność'
}


def weather_message(location=default_city):
    data = get_current_weather_from_city_name(location)
    main_data = data['main']
    additional_data = data['weather']
    message = discord.Embed(
        title=f'Pogoda {location}',
        description=f'Obecna pogoda w mieście {location}.',
        color=color
    )
    for key in key_features:
        message.add_field(
            name=key_features[key],
            value=str(main_data[key]),
            inline=False
        )
    message.add_field(
        name='Warunki pogodowe',
        value=str(additional_data[0]['description']),
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

