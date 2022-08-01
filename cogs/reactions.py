import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get

class reactions(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        channel = reaction.message.channel
        await channel.send(user.name + " added: " + reaction.emoji)
    
    @commands.command(name='ras')
    async def ras(self, ctx, type):
        if type == 'create':
            pass

def setup(bot):
    bot.add_cog(reactions(bot))