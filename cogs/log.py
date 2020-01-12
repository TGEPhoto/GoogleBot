import discord
from discord.ext import commands

import keys
from util import functions


class Log(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_snootyboop_land(self, guild):
        return guild.id == 658737319943340047

    async def trigger_log_webhook(self, embed, username, avatar_url=None, guild=None):
        try:
            webhook = discord.Webhook.from_url(keys.log_webhook,
                                               adapter=discord.AsyncWebhookAdapter(self.bot.client_session))
            await webhook.send(embed=embed, username=username, avatar_url=avatar_url)
        except:
            await guild.get_channel(660760578423390209).send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not self.is_snootyboop_land(after.guild):
            return

        if after.author.bot:
            return

        embed = discord.Embed(title=f'Message by {after.author} in #{after.channel} was edited',
                              description=f'**Before**:\n{before.clean_content}\n**After**:\n{after.clean_content}',
                              color=functions.random_discord_color(), timestamp=after.edited_at)
        embed.set_author(name=after.author, icon_url=after.author.avatar_url)
        embed.add_field(name='Channel', value=after.channel.mention)
        await self.trigger_log_webhook(embed, username='Message edited', guild=after.guild)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not self.is_snootyboop_land(message.guild):
            return

        if message.author.bot:
            return

        embed = discord.Embed(title=f'Message by {message.author} in #{message.channel} was deleted',
                              description=message.clean_content,
                              color=functions.random_discord_color(), timestamp=message.created_at)
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name='Channel', value=message.channel.mention)
        await self.trigger_log_webhook(embed, username='Message edited', guild=message.guild)


def setup(bot):
    bot.add_cog(Log(bot))
