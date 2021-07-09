import discord
from discord.ext import commands
from discord_slash import cog_ext

class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Sends Pong')
    async def ping(self, ctx):
        await ctx.send('pong')

    @cog_ext.cog_slash(name='Ping', description='Sends Pong')
    async def ping(self, ctx):
        await ctx.send('pong')


def setup(bot):
    bot.add_cog(Cogs(bot))
