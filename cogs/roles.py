import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get

class roles(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='giverole', pass_context = True)
    @commands.has_permissions(manage_roles = True)
    async def giverole(self, ctx, user : discord.Member, *, role: discord.Role):
        if role in user.roles:
            await ctx.send(f"{user.mention} already has the @{role} role")
        else:
            await user.add_roles(role)
            await ctx.send(f"{user.mention} has been given the @{role} role")

    @giverole.error
    async def role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            pass
    
    @commands.command(name='takerole', pass_context = True)
    @commands.has_permissions(manage_roles = True)
    async def takerole(self, ctx, user : discord.Member, *, role: discord.Role):
        if role in user.roles:
            await user.remove_roles(role)
            await ctx.send(f"{user.mention} no longer has the @{role} role")
        else:
            await ctx.send(f"{user.mention} does not have the @{role} role")

    @takerole.error
    async def role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            pass

def setup(bot):
    bot.add_cog(roles(bot))