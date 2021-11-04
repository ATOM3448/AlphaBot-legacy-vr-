import asyncio
import discord
import json
import codecs
import os
import infoCommand
from config import settings
from FMFresurses import res

async def changebal(ctx, when, how):
    if(when == 'общий'):
        await ctx.send("Ахуел?")
        return
    user = str(ctx.message.author.id)
    contents = []
    with codecs.open(f'UsersData/{user}/{when}.txt', 'r+', 'utf-8') as file_object:
        count = 0
        while True:
            contents.append(file_object.readline())
            if not contents[count]:
                break
            count += 1
    newBal = 0
    size = len(contents) - contents.index('СКЛАД\n') - 2
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
    await ctx.send('Выполнено')