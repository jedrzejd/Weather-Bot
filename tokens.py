from dotenv import load_dotenv
import os

load_dotenv()

WEATHER_TOKEN = os.getenv('WEATHER_TOKEN')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
