import discord
from tokens import DISCORD_TOKEN
from weather import weather_message, error_message
from data_preprocessing import replace

PREFIX__weather = 'pogoda'
# PREFIX__raining = ['czy bedzie padac?', 'będzie padac?']
# PREFIX__rower = ['rower', 'pogoda na rower', 'rowerczan']

client = discord.Client()


def text_in_message(text):

    if PREFIX__weather in text.lower():
        return 0
    # elif text.lower() in PREFIX__raining:
    #     return 1
    # elif text.lower() in PREFIX__rower:
    #     return 2
    return 3


@client.event
async def on_message(message):
    if message.author != client.user:
        msg = message.content
        msg = replace(msg)
        nb_q = text_in_message(msg)
        if nb_q == 0:
            try:
                if '.' in msg:
                    location = msg.split('.')[-1]
                    await message.channel.send(embed=weather_message(location))
                else:
                    await message.channel.send(embed=weather_message())
            except KeyError:
                location = msg.split('.')[-1]
                await message.channel.send(embed=error_message(location))
        else:
            return


client.run(DISCORD_TOKEN)
