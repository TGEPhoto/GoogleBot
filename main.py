import aiohttp
import discord
import os
from keys import bot as BOT_TOKEN
from discord.ext import commands

bot = commands.Bot(command_prefix=".", owner_ids=[611540017000480773, 529535587728752644])

@bot.command()
async def guild(ctx):
    """
    Sends invite to bot development guild in dm
    """
    embed = discord.Embed(title="Do you want to contribute to development of the bot?",
                          description="Come and join our guild!\nSuggest ideas for new commands and help us make the bot better.",
                          colour=0x0f9d58)
    embed.add_field(name="Invite", value="https://discord.gg/G996vhj")
    await ctx.send(embed=embed)

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
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='snoot')
    await member.add_roles(role)
    print(f'{member} has joined')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('use .help'))
    print('Bot is online.')
    bot.client_session = aiohttp.ClientSession()


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


@bot.command(aliases=['exit'])
@commands.is_owner()
async def close(ctx):
    await ctx.send('Closing...')
    await bot.client_session.close()
    await bot.logout()


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(BOT_TOKEN)