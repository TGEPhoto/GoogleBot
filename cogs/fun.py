import discord
import random
from discord.ext import commands

RES_DIR = 'res'


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poop(self, ctx, member: discord.Member):
        """
        Poops the person. Very shitty command
        """
        await ctx.send(f'\N{PILE OF POO}\N{PILE OF POO}\N{PILE OF POO} {ctx.author.mention} has pooped on {member.name}#{member.discriminator}')

    @poop.error
    async def poop_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You have to poop someone!')

    @commands.command()
    async def say(self, ctx, *, message):
        """
        Makes the bot say something
        """
        await ctx.channel.trigger_typing()
        sentMessage = await ctx.send(message)
        await ctx.message.delete()

    @commands.command()
    async def leesong(self, ctx):
        """
        Sends link to The STD Song
        """
        await ctx.send('https://youtu.be/uukvEcd25oQ')

    @commands.command()
    async def kidnap(self, ctx, member: discord.Member):
        """
        Apparently kidnaps the member
        """
        await ctx.send(f'\N{IMP}\N{PISTOL} Get in the back of my van, you whore! {member.name}#{member.discriminator}')

    @kidnap.error
    async def kidnap_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You gotta mention someone!')

    @commands.command()
    async def tip(self, ctx):
        """
        Sends random tips
        """
        with open(f'{RES_DIR}/tips.txt', 'r') as f:
            await ctx.send(random.choice(f.readlines()))

    @commands.command()
    async def joke(self, ctx):
        """
        Sends terrible dad jokes
        """
        with open(f'{RES_DIR}/joke.txt', 'r') as f:
            await ctx.send(random.choice(f.readlines()))
    
    @commands.command()
    async def anthem(self, ctx):
        """
        Sends USSR anthem
        """
        await ctx.send('https://www.youtube.com/watch?v=U06jlgpMtQs')

    @commands.command()
    async def cookie(self, ctx, member: discord.Member):
        """
        Sends a cookie to the user
        """
        await ctx.send(f'\N{COOKIE}\N{COOKIE}\N{COOKIE} {member.name}#{member.discriminator} has received a cookie from {ctx.author.mention}! *nom nom nom*')

    @cookie.error
    async def cookie_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You didn't tell me who to give the cookie! Maybe you should get cookies instead <3")

    @commands.command()
    async def boop(self, ctx, member: discord.Member):
        """
        Boops a member
        """
        await ctx.send(f'*boop boop* {ctx.author.mention} has booped {member.name}#{member.discriminator}!')

    @boop.error
    async def boop_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You didn't tell me who to boop! Maybe we should boop you instead?")

def setup(bot):
    bot.add_cog(Fun(bot))