import asyncio
import json
import codecs
import os
import discord
import getgamepanelcommandraces
from discord.ext import commands
from config import settings
from FMFresurses import res

async def getgamepanel(ctx, bot):
    guild = bot.get_guild(652220049012031488)
    roles = ctx.author.roles
    check = 0
    for i in roles:
        if(i == guild.get_role(655340889530433536)): #Конкистадоры
            await getgamepanelcommandraces.getgamepanelkonkisti(ctx, bot)
            check = 1
            break
        if(i == guild.get_role(653246548762951680)): #Матрикс
            check = 1
            break
        if(i == guild.get_role(652224021533818912)): #Крюксы
            check = 1
            break
        if(i == guild.get_role(760752746965762078)): #Биомехи
            check = 1
            break
        if(i == guild.get_role(778016234368794667)): #Спектралы
            check = 1
            break
        if(i == guild.get_role(674317063246053387)): #Симелянты
            check = 1
            break
        if(i == guild.get_role(675802459691679766)): #Ящуры
            check = 1
            break
    if(check == 0):
        await ctx.send('Вы не являетеесь игроком!')