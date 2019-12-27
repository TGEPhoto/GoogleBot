import discord
import random
from discord.ext import commands

class Love(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["3"])
    async def love(self, ctx):
        """
        Sends random love messages
        """
        responses = ['You are beautiful!',
                    'You are epic',
                    'I love you uwu',
                    'You are wonderful',
                    'I love you cutie',
                    'You are cute',
                    'ily comrade',
                    'Message my creator to add more love!']
        await ctx.send(f'{random.choice(responses)}')

def setup(client):
    client.add_cog(Love(client))
