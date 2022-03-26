import asyncio
import codecs
import os
import discord
import infoCommand
import changebalanceCommand
import newregCommand
import nextturnCommand
import gamepanelCommand
import GetUserInfo
from discord.ext import commands
from config import settings
from FMFresurses import res

bot = commands.Bot(command_prefix = settings['prefix'])

#+количество ресурса
@bot.command() 
async def changebalance(ctx, when, how):
    await changebalanceCommand.changebal(ctx, when, how)

#тест класса
@bot.command()
@commands.has_permissions(administrator=True)
async def clastes(ctx):
    await ctx.send(str(GetUserInfo.getProduction(ctx.message.author.id)))

#информация о игроке
@bot.command()
async def info(ctx):
    await infoCommand.inf(ctx, bot)

#информация о игроке для админов
@bot.command()
@commands.has_permissions(administrator=True)
async def infoFA(ctx, userpin):
    await infoCommand.infFA(ctx, bot, userpin)

#новая регистрация
@bot.command()
@commands.has_permissions(administrator=True)
async def newreg(ctx):
    await newregCommand.newreg(ctx, bot)

#игровая панель
@bot.command()
async def gamepanel(ctx):
    await gamepanelCommand.getgamepanel(ctx, bot)

#следующий ход
@bot.command()
async def nexttrun(ctx):
    await nextturnCommand.nt(ctx, bot)
    
#действия на реакции
@bot.event
async def on_raw_reaction_add(self):
    await newregCommand.roleset(bot, self)

bot.run(settings['token'])