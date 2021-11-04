import asyncio
import discord
import json
import codecs
import os
from discord.embeds import Embed
from FMFresurses import res

async def inf(ctx, bot):
    user = ctx.message.author.id
    await ctx.send("Напишите склад чего выхотите посмотреть(Название планеты/общий)")
    check = lambda m: m.author == ctx.author and m.channel == ctx.channel
    try:
        planet = await bot.wait_for('message', check=check, timeout=30)
    except asyncio.TimeoutError:
        await ctx.send('Команда вывода информации отменена. Время вышло')
        return
    try:
        contents = []
        fileway = f'UsersData/{user}/{planet.content.lower()}.txt'
        with codecs.open(fileway, 'r+', 'utf-8') as file_object:
            count = 0
            while True:
                contents.append(file_object.readline())
                if not contents[count]:
                    break
                count += 1
        size = contents.index('КОРАБЛИ\n') - contents.index('СКЛАД\n') - 1
        cargo = ''
        count = contents.index('СКЛАД\n') + 1
        for i in range(size):

            cargo += f'{contents[count]}\n'
            count += 1
        turn = ''
        for i in contents:
            if(i[0]+i[1]+i[2] == 'ХОД'):
                index = contents.index(i)
                break
        for st in contents[index]:
            if((st != 'Х') and (st != 'О') and (st != 'Д') and (st != ' ') and (st != '-')):
                turn += st
        planeti = ''
        for i in contents:
            if(i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6] == 'ПЛАНЕТА'):
                index = contents.index(i)
                break
        for st in contents[index]:
            if((st != 'П') and (st != 'Л') and (st != 'А') and (st != ' ') and (st != 'Н') and (st != 'Е') and (st != 'Т') and (st != '-')):
                planeti += st
        embed1 = discord.Embed(title='Информация о игроке', description=f'{contents[contents.count("РАСА")]}', colour=0x008b)
        embed1.add_field(name="ХОД", value=f'{turn}', inline=False)
        embed1.add_field(name="ПЛАНЕТА", value=f'{planeti}', inline=False)
        embed1.add_field(name="СКЛАД", value=f'{cargo}', inline=False)

        panel1 = await ctx.send(embed = embed1)

        race = ''
        for i in contents:
            if(i[0]+i[1]+i[2]+i[3] == 'РАСА'):
                maxi = len(i)
                for k in range(maxi-7):
                    race += i[k+7]
                break
        
        if(race != 'КОНКИСТАДОРЫ\n'):
            await ctx.send('Вывод зданий')

        indexOfStartShips = 0
        for i in contents:
            if(i[0] != 'К'):
                continue
            if(i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6] == 'КОРАБЛИ'):
                indexOfStartShips = contents.index(i)
                break
        indexOfEndShips = 0
        for i in contents:
            if(i[0] != 'Д'):
                continue
            if(i[0]+i[1]+i[2]+i[3]+i[4]+i[5] == 'ДОБЫЧА'):
                indexOfEndShips = contents.index(i)
                break
        steeps = indexOfEndShips - indexOfStartShips - 1
        sheeps = ''
        for i in range(steeps):
            sheeps += contents[i+indexOfStartShips+1]
        
        embed3 = discord.Embed(title='Корабли', description=f'{sheeps}', colour=0x008b)
        panel3 = await ctx.send(embed = embed3)


        income = ''
        indexOfStartIncome = 0
        indexOfEndIncome = 0
        for i in contents:
            if(i[0] != 'Д'):
                continue
            if(i[0] + i[1] + i[2] + i[3] + i[4] + i[5] == 'ДОБЫЧА' ):
                indexOfStartIncome = contents.index(i)
                break
        for i in contents:
            if(i[0] != 'В'):
                continue
            if(i[0] + i[1] + i[2] + i[3] + i[4] + i[5] + i[6] + i[7] + i[8] + i[9] == 'В-ПРОЦЕССЕ' ):
                indexOfEndIncome = contents.index(i)
                break  
        steeps = indexOfEndIncome - indexOfStartIncome - 1
        for i in range(steeps):
            income += contents[i+indexOfStartIncome+1]
        
        embed4 = discord.Embed(title='ДОБЫЧА', description=f'{income}', colour=0x008b)
        panel4 = await ctx.send(embed = embed4)

        conten = []
        with codecs.open(f'UsersData/{user}/исследования.txt', 'r+', 'utf-8') as f:
            count = 0
            while True:
                conten.append(f.readline())
                if not conten[count]:
                    break
                count += 1
        researchlist = ''
        for i in conten:
            if(conten.index(i) == 0):
                continue
            researchlist += i
        
        embed5 = discord.Embed(title='Исследования', description=f'{researchlist}', colour=0x008b)
        panel5 = await ctx.send(embed = embed5)

    except FileNotFoundError:
        await ctx.send("Планета не найдена.")


async def infFA(ctx, bot, userpin):
    user = ''
    for i in userpin:
        if((i == '@') or (i == '<') or (i == '!') or (i == '>')):
            continue
        user += i

    await ctx.send("Напишите склад чего выхотите посмотреть(Название планеты/общий)")
    check = lambda m: m.author == ctx.author and m.channel == ctx.channel
    try:
        planet = await bot.wait_for('message', check=check, timeout=30)
    except asyncio.TimeoutError:
        await ctx.send('Команда вывода информации отменена. Время вышло')
        return
    try:
        contents = []
        fileway = f'UsersData/{user}/{planet.content.lower()}.txt'
        with codecs.open(fileway, 'r+', 'utf-8') as file_object:
            count = 0
            while True:
                contents.append(file_object.readline())
                if not contents[count]:
                    break
                count += 1
        size = contents.index('КОРАБЛИ\n') - contents.index('СКЛАД\n') - 1
        cargo = ''
        count = contents.index('СКЛАД\n') + 1
        for i in range(size):

            cargo += f'{contents[count]}\n'
            count += 1
        turn = ''
        for i in contents:
            if(i[0]+i[1]+i[2] == 'ХОД'):
                index = contents.index(i)
                break
        for st in contents[index]:
            if((st != 'Х') and (st != 'О') and (st != 'Д') and (st != ' ') and (st != '-')):
                turn += st
        planeti = ''
        for i in contents:
            if(i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6] == 'ПЛАНЕТА'):
                index = contents.index(i)
                break
        for st in contents[index]:
            if((st != 'П') and (st != 'Л') and (st != 'А') and (st != ' ') and (st != 'Н') and (st != 'Е') and (st != 'Т') and (st != '-')):
                planeti += st
        embed1 = discord.Embed(title='Информация о игроке', description=f'{contents[contents.count("РАСА")]}', colour=0x008b)
        embed1.add_field(name="ХОД", value=f'{turn}', inline=False)
        embed1.add_field(name="ПЛАНЕТА", value=f'{planeti}', inline=False)
        embed1.add_field(name="СКЛАД", value=f'{cargo}', inline=False)

        panel1 = await ctx.send(embed = embed1)

        race = ''
        for i in contents:
            if(i[0]+i[1]+i[2]+i[3] == 'РАСА'):
                maxi = len(i)
                for k in range(maxi-7):
                    race += i[k+7]
                break
        
        if(race != 'КОНКИСТАДОРЫ\n'):
            await ctx.send('Вывод зданий')

        indexOfStartShips = 0
        for i in contents:
            if(i[0] != 'К'):
                continue
            if(i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6] == 'КОРАБЛИ'):
                indexOfStartShips = contents.index(i)
                break
        indexOfEndShips = 0
        for i in contents:
            if(i[0] != 'Д'):
                continue
            if(i[0]+i[1]+i[2]+i[3]+i[4]+i[5] == 'ДОБЫЧА'):
                indexOfEndShips = contents.index(i)
                break
        steeps = indexOfEndShips - indexOfStartShips - 1
        sheeps = ''
        for i in range(steeps):
            sheeps += contents[i+indexOfStartShips+1]
        
        embed3 = discord.Embed(title='Корабли', description=f'{sheeps}', colour=0x008b)
        panel3 = await ctx.send(embed = embed3)


        income = ''
        indexOfStartIncome = 0
        indexOfEndIncome = 0
        for i in contents:
            if(i[0] != 'Д'):
                continue
            if(i[0] + i[1] + i[2] + i[3] + i[4] + i[5] == 'ДОБЫЧА' ):
                indexOfStartIncome = contents.index(i)
                break
        for i in contents:
            if(i[0] != 'В'):
                continue
            if(i[0] + i[1] + i[2] + i[3] + i[4] + i[5] + i[6] + i[7] + i[8] + i[9] == 'В-ПРОЦЕССЕ' ):
                indexOfEndIncome = contents.index(i)
                break  
        steeps = indexOfEndIncome - indexOfStartIncome - 1
        for i in range(steeps):
            income += contents[i+indexOfStartIncome+1]
        
        embed4 = discord.Embed(title='ДОБЫЧА', description=f'{income}', colour=0x008b)
        panel4 = await ctx.send(embed = embed4)

        conten = []
        with codecs.open(f'UsersData/{user}/исследования.txt', 'r+', 'utf-8') as f:
            count = 0
            while True:
                conten.append(f.readline())
                if not conten[count]:
                    break
                count += 1
        researchlist = ''
        for i in conten:
            if(conten.index(i) == 0):
                continue
            researchlist += i
        
        embed5 = discord.Embed(title='Исследования', description=f'{researchlist}', colour=0x008b)
        panel5 = await ctx.send(embed = embed5)

    except FileNotFoundError:
        await ctx.send("Планета не найдена.")