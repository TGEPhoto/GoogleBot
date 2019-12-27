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
                    'Message my creator to add more love!',
                    'You’re more helpful than you realize.',
                    'If cartoon bluebirds were real, a bunch of them would be sitting on your shoulders singing right now.',
                    'You are making a good difference in the world just by existing.',
                    'Your existence alone makes peoples days better',
                    'You bring out the best in other people',
                    'When you are not afraid to be yourself is when you are most incredible',
                    'I wish you realized how beautiful you are inside and out',
                    'You are more fun than a ball pit filled with candy. And seriously, what could be more fun than that?',
                    'You are better than a triple-scoop ice cream cone. Even with rainbow sprinkles',
                    'This server is better because you’re in it',
                    'You are more fun than bubble wrap',
                    'You should be thanked more often. Thank you!']
        await ctx.send(f'{random.choice(responses)}')

def setup(client):
    client.add_cog(Love(client))
