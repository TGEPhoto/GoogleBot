import discord
import os
from keys import bot as BOT_TOKEN
from discord.ext import commands

bot = commands.Bot(command_prefix=".", owner_ids=[611540017000480773, 529535587728752644])


@bot.command()
async def info(ctx):
    """
    Sends info about the bot
    """
    embed = discord.Embed(title="Info about Google bot",
                          description='Library: discord.py\nCreator: TGEPhoto#9952\nOpen Source: Yes\nRepo can be found with .repo',
                          colour=0x4285f4)
    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('use .help'))
    print('Bot is online.')


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('\N{WHITE HEAVY CHECK MARK}')


@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send('\N{WHITE HEAVY CHECK MARK}')


@bot.command(aliases=['close'])
@commands.is_owner()
async def close(ctx):
    await bot.logout()


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(BOT_TOKEN)
