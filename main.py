import discord
import os
from keys import bot as BOT_TOKEN
from discord.ext import commands
from helper import member as member_role

client = commands.Bot(command_prefix = "<", owner_ids=[611540017000480773])

@client.event
async def on_member_join(member):
    await member.add_roles(member_role)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('use <help'))
    print('Bot is online.')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(BOT_TOKEN)