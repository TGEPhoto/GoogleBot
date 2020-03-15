import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=2):
        """
        Purges given amount of messages
        """
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """
        Bans a user and dms the reason
        """
        msg = "You have been banned from Google"
        if reason:
            msg += f" for {reason}"

        try:
            await member.send(msg)
        except discord.Forbidden:
            await ctx.send("I can't message that user")

        await ctx.send(f'{member.name}#{member.discriminator} has been banned!')
        await member.ban(reason=reason)
    
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You didn't give me a member to ban!")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """
        Kicks a user and dms the reason
        """
        msg = "You have been kicked from Google"
        if reason:
            msg += f" for {reason}"

        try:
            await member.send(msg)
        except discord.Forbidden:
            await ctx.send("I can't message that user")

        await ctx.send(f'{member.name}#{member.discriminator} has been kicked!')
        await member.kick(reason=reason)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You didn't give me a member to kick!")

def setup(client):
    client.add_cog(Moderation(client))
