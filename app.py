import discord
import ezcord
import configparser

bot = ezcord.Bot(intents=discord.Intents.all())
bot.load_extension('cogs')

config = configparser.ConfigParser()
config.read('config.ini')
token = config['KEYS']['discord_bot_token']

bot.run(token)
