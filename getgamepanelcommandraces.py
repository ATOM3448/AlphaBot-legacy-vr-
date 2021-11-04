import asyncio
import json
import codecs
import os
import discord
from discord.ext import commands
from config import settings
from FMFresurses import res

async def getgamepanelkonkisti(ctx, bot):
    embed1 = discord.Embed(title='Панель игрока', description='Тут вы можете легко управляеть своей империей', colour=0x008b)
    embed1.add_field(name="ХОД", value=f'', inline=False)