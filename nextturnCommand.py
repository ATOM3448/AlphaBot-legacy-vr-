import asyncio
import json
import codecs
import os
import discord
import infoCommand
import changebalanceCommand
import newregCommand
import nextturnCommand
from discord.ext import commands
from config import settings
from FMFresurses import res

async def nt(ctx, bot):
    guild = bot.get_guild(652220049012031488)
    filename = []
    user = ctx.user_id
    #вапускаем процесс занесения всех планет в список
        #внесение всех планет в КЖ
    category = guild.get_channel(868127161435971634)
    for channel in category.channels:
        if(channel.name != 'космос'):
            filename.append(channel.name)
        else:
            filename.append(f'{channel.name}1')
        #внесение всех планет в ГГ
    category = guild.get_channel(868127210119245824)
    for channel in category.channels:
        if(channel.name != 'космос'):
            filename.append(channel.name)
        else:
            filename.append(f'{channel.name}2')
        #внесение всех планет в ЗП
    category = guild.get_channel(868127269498019860)
    for channel in category.channels:
        if(channel.name != 'космос'):
            filename.append(channel.name)
        else:
            filename.append(f'{channel.name}3')
        #внесение всех планет в ЖЦ
    category = guild.get_channel(655043870064771073)
    for channel in category.channels:
        if(channel.name != 'космос'):
            filename.append(channel.name)
        else:
            filename.append(f'{channel.name}4')
    #часть с вычислениями
    #повторяем пока не пройдём все файлы
    for when in filename:
        #удалить
        how = 1
        #сюда записываем содержимое файла
        contents = []
        with codecs.open(f'UsersData/{user}/{when}.txt', 'r+', 'utf-8') as file_object:
            count = 0
            while True:
                contents.append(file_object.readline())
                if not contents[count]:
                    break
                count += 1
        newBal = 0
        size = contents.index('К') - contents.index('СКЛАД\n') - 2
        count = contents.index('СКЛАД\n') + 1
        cargo = ''
        for i in range(size):
            gostart = ''  
            howInt = int(how)
            num = ''
            indexOfNums = contents[count].index('-') + 2
            while(len(contents[count]) > indexOfNums):
                num += contents[count][indexOfNums]
                indexOfNums += 1
            contensInt = int(num)
            newBal = contensInt + howInt
            for ch in contents[count]:
                if ch != ' ':
                    gostart += ch
                else:
                    gostart += " - "
                    break
            contents[count] = gostart + str(newBal) + '\n'

            count += 1
        with  codecs.open(f'UsersData/{user}/{when}.txt', 'w', 'utf-8') as file_object:
            for i in contents:
                file_object.writelines(i)