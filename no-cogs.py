import discord
from discord.ext import commands
from discord_slash import SlashCommand

bot = commands.Bot(command_prefix = '>')
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():   
    print('Bot Is Ready')   

@bot.command(description='Sends Pong')
async def ping(ctx):
    await ctx.send('pong')
    
@slash.slash(name = 'Ping', description='Sends Pong')
async def ping(ctx):
    await ctx.send('pong')

bot.run('TOKEN HERE')
