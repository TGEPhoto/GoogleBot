from random import randint

import discord


def random_discord_color():
    return discord.Color(value=randint(0, 16777215))
