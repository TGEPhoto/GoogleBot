from discord.ext import commands
import random

RES_DIR = 'res'


class Love(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def love(self, ctx):
        """Sends random love message"""

        with open(f'{RES_DIR}/love.txt', 'r') as f:
            await ctx.send(random.choice(f.readlines()))

    @commands.command()
    async def positivity(self, ctx):
        """Sends a random positive message"""

        with open(f'{RES_DIR}/positivity.txt', 'r') as f:
            await ctx.send(random.choice(f.readlines()))


def setup(bot):
    bot.add_cog(Love(bot))
