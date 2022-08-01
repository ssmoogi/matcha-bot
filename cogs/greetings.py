import discord
from discord.ext import commands

class greetings(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='hello', help='-says hello')
    async def hello(self, ctx):
        await ctx.send('hello')

    # for events @commands.Cog.listener()

def setup(bot):
    bot.add_cog(greetings(bot))