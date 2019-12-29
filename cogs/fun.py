import discord
import random
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tip(self, ctx):
        """
        Sends random tips
        """
        responses = ['Clean your camera lens before taking a photo.',
                    'Delete those blurry photos from your gallery.',
                    'Delete the apps you dont use at all.',
                    'Have you turned data off and switched to wifi?',
                    'Download Google Camera.',
                    'Remember to test your code!',
                    'Turn on dark mode, especially if you are using an AMOLED screen.',
                    'uwu this is weird',
                    'Be careful if your phone is cracked because you might cut your fingers.',
                    'Message my creator to add more tips!']
        await ctx.send(f'{random.choice(responses)}')

    @commands.command()
    async def cookie(self, ctx, member: discord.Member):
        """
        Sends a cookie to the user
        """
        await ctx.send(f'{member.name}#{member.discriminator} has recieved a cookie from {ctx.author.mention}!')
    
def setup(client):
    client.add_cog(Fun(client))
