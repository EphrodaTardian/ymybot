# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2020, Yazılımcıların Mola Yeri (ymy-discord)
#

import discord
from discord.ext import commands


class Fun(commands.Cog):
    """The description for Fun goes here."""

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Fun(bot))