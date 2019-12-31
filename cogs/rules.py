import discord
from discord.ext import commands

class Rules(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rule1(self, ctx):
        embed = discord.Embed(title="Rule 1",
                              description="Snoots may only be booped on with the consent of the boopee.",
                              colour=0xdb4437)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def rule2(self, ctx):
        embed = discord.Embed(title="Rule 2",
                              description="Go to bed on your bed time.",
                              colour=0xdb4437)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def rule3(self, ctx):
        embed = discord.Embed(title="Rule 3",
                              description="Stay hydrated and don’t forget to eat!",
                              colour=0xdb4437)
        await ctx.send(embed=embed)

    @commands.command()
    async def rule4(self, ctx):
        embed = discord.Embed(title="Rule 4",
                              description="Be honest when you’re sad. Its okay to talk about your feelings :)",
                              colour=0xdb4437)
        await ctx.send(embed=embed)

    @commands.command()
    async def rule5(self, ctx):
        embed = discord.Embed(title="Rule 5",
                              description="Be kind here! This is a place of kindness!",
                              colour=0xdb4437)
        await ctx.send(embed=embed)

    @commands.command()
    async def rule6(self, ctx):
        embed = discord.Embed(title="Rule 6",
                              description="Ask before you invite someone please!",
                              colour=0xdb4437)
        await ctx.send(embed=embed)

    @commands.command()
    async def rule7(self, ctx):
        embed = discord.Embed(title="Rule 7",
                              description="Love yourself! You are amazing just the way you are!",
                              colour=0xdb4437)
        await ctx.send(embed=embed)

    @commands.command()
    async def rule8(self, ctx):
        embed = discord.Embed(title="Rule 8",
                              description="Try to keep things positive. Lets make sure everyone is having a good time and feels safe!",
                              colour=0xdb4437)
        await ctx.send(embed=embed)

    @commands.command()
    async def rule9(self, ctx):
        embed = discord.Embed(title="Rule 9",
                              description="Keep politics out of discussions",
                              colour=0xdb4437)
        await ctx.send(embed=embed)

    @commands.command()
    async def rule10(self, ctx):
        embed = discord.Embed(title="Rule 10",
                              description="Ginger jokes will give you 10 epic points. Alexa jokes give you negative 10",
                              colour=0xdb4437)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Rules(bot))