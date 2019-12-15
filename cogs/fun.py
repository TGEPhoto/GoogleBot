import discord
import random
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tip(self, ctx):
        responses = ['Clean your camera lens before taking a photo.',
                    'Delete those blurry photos from your gallery.',
                    'Delete the apps you dont use at all.',
                    'Have you turned data off and switched to wifi?',
                    'Download Google Camera.',
                    'Remember to test your code!',
                    'Turn on dark mode, especially if you are using an AMOLED screen.',
                    'uwu this is weird',
                    'Be careful if your phone is cracked because you might cut your fingers.']
        await ctx.send(f'{random.choice(responses)}')

def setup(client):
    client.add_cog(Fun(client))
