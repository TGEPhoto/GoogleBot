import discord
from discord.ext import commands
import random
import re
from util import functions

RES_DIR = 'res'


class Love(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.is_image_regex = re.compile(r".*\.(jpg|png|gif)$")

    @commands.command()
    async def love(self, ctx):
        """Sends random love message"""

        with open(f'{RES_DIR}/love.txt', 'r') as f:
            await ctx.send(random.choice(f.readlines()))

    @commands.command()
    async def positivity(self, ctx):
        """Sends a random positive message"""

        with open(f'{RES_DIR}/positivity.txt', 'r') as f:
            await ctx.send(random.choice(f.readlines()))

    @commands.command(name='wholesomeme', aliases=['wm'])
    async def wholesome_meme(self, ctx):

        search = random.choice(['wholesomememes', 'wholesomememes'])

        await ctx.channel.trigger_typing()
        async with self.bot.client_session.get(f'http://reddit.com/r/{search}/hot/.json',
                                              headers={'User-agent': 'Chrome'}) as res:
            json = await res.json()

            posts = json["data"]["children"]
            post = posts[random.randint(0, len(posts) - 1)]['data']

            if post['over_18'] and not ctx.channel.is_nsfw():
                return

            embed = discord.Embed(title=post["title"], url=f'https://reddit.com{post["permalink"]}',
                                  color=functions.random_discord_color())
            embed.set_author(name=f'u/{post["author"]}')
            embed.set_footer(text=post['subreddit_name_prefixed'])

            if post['is_self']:
                text = post['selftext']
                embed.description = text[:800] if len(text) < 800 else f'{text[:800]} **--Snippet--**'
            elif re.match(self.is_image_regex, post['url']):
                embed.set_image(url=post['url'])

            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Love(bot))
