import discord
from discord.ext import commands
import util.functions as functions


class Rules(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.rules = None

    @commands.command()
    async def rule(self, ctx, *, number: int):
        if self.rules is None:
            print('yes')
            channel = ctx.guild.get_channel(658739523370483742)
            message = await channel.history(limit=1).flatten()
            message = message[0]

            def filter_pred(item: str):
                split_rule = item.split(' ')
                split_rule.pop(0)
                return ' '.join(split_rule).strip()

            split = discord.utils.escape_markdown(message.content).split('\n')
            self.rules = [filter_pred(x) for x in split if bool(x)]

        embed = discord.Embed(
            title=f"Rule {number}",
            description=self.rules[number - 1],
            colour=functions.random_discord_color(),
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Rules(bot))
