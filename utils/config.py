import os

from dotenv import load_dotenv


# load in the environment variables defined in the .env file
load_dotenv()

DISCORD_GUILD = os.getenv('DISCORD_GUILD')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
WELCOME_CHANNEL = os.getenv('WELCOME_CHANNEL')
