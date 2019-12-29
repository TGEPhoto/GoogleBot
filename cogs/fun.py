import discord
import random
from discord.ext import commands

RES_DIR = 'res'


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tip(self, ctx):
        """
        Sends random tips
        """
        with open(f'{RES_DIR}/tips.txt', 'r') as f:
            await ctx.send(random.choice(f.readlines()))

    @commands.command()
    async def cookie(self, ctx, member: discord.Member):
        """Sends a cookie to the user"""

        await ctx.send(f'{member.name}#{member.discriminator} has received a cookie from {ctx.author.mention}!')


def setup(bot):
    bot.add_cog(Fun(bot))
