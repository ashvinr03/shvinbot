import os
from keep_alive import keep_alive
from discord.ext import commands

#bot command and ignore capitalization
bot = commands.Bot(
	command_prefix=";",
	case_insensitive=True
)

bot.author_id = 285832442592624641

#prepares bot and sets load message
@bot.event 
async def on_ready():
    print("I'm in")
    print(bot.user)

#sets cog example extension
extensions = [
	'cogs.cog_example'
]

#forces bot on and loads all extensions
if __name__ == '__main__':
	for extension in extensions:
		bot.load_extension(extension)

#final preparation, set botkey, and starts bot
keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)
