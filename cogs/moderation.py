import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def purge(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Moderation(client))
