import asyncio
import discord
import json
import codecs
import os
import shutil
from FMFresurses import res

async def regKon(self, bot):
    newL = '\n'
    guild = bot.get_guild(652220049012031488)
    filename = []
    user = self.user_id
    #вапускаем процесс занесения всех планет в список
        #внесение всех планет в КЖ
    category = guild.get_channel(868127161435971634)
    for channel in category.channels:
        if(channel.name != 'космос'):
            if(channel.name == 'пояс-астероидов'):
                filename.append(f'{channel.name}1')
                continue
            filename.append(channel.name)
        else:
            filename.append(f'{channel.name}1')
        #внесение всех планет в ГГ
    category = guild.get_channel(868127210119245824)
    for channel in category.channels:
        if(channel.name != 'космос'):
            if(channel.name == 'пояс-астероидов'):
                filename.append(f'{channel.name}2')
                continue
            filename.append(channel.name)
        else:
            filename.append(f'{channel.name}2')
        #внесение всех планет в ЗП
    category = guild.get_channel(868127269498019860)
    for channel in category.channels:
        if(channel.name != 'космос'):
            if(channel.name == 'пояс-астероидов'):
                filename.append(f'{channel.name}3')
                continue
            filename.append(channel.name)
        else:
            filename.append(f'{channel.name}3')
        #внесение всех планет в ЖЦ
    category = guild.get_channel(655043870064771073)
    for channel in category.channels:
        if(channel.name != 'космос'):
            if(channel.name == 'пояс-астероидов'):
                filename.append(f'{channel.name}4')
                continue
            filename.append(channel.name)
        else:
            filename.append(f'{channel.name}4')
    try:
        os.makedirs(f'UsersData/{user}')
    except FileExistsError:
        try:
            shutil.rmtree(f'UsersData/{user}')
        except PermissionError:
            return
        os.makedirs(f'UsersData/{user}')

    with codecs.open('UsersData/RegistredPlayers.txt') as file_object:
        contents = file_object.read()
    for na in filename:
        with codecs.open(f'UsersData/{user}/{na}.txt', 'w', 'utf-8') as f:
            f.write(f'РАСА - КОНКИСТАДОРЫ\nХОД - 0\nПЛАНЕТА - {na}\nСКЛАД\n{res["zelezo"]} - 0\n{res["zest"]} - 0\n{res["titan"]} - 0\n{res["vjoblost"]} - 0\n{res["gugol"]} - 0\n{res["gas"]} - 0\n{res["energy"]} - 0\n{res["kamen1"]} - 0\n{res["kamen2"]} - 0\n{res["kamen3"]} - 0\n{res["kamen4"]} - 0\n{res["sverol"]} - 0\n{res["relik"]} - 0\n{res["voda"]} - 0\n{res["naselenie"]} - 0\n{res["mikrobot"]} - 0\n{res["moh"]} - 0\n{res["sol"]} - 0\n{res["antipizdec"]} - 0\n{res["nanohujna"]} - 0\n'+
            f'КОРАБЛИ\nМусорщик - 0\nКаменьщик - 0\nЛегкий-Верфятник - 0\nИстребитель-Капля - 0\nКаравелла - 0\nСредний-Верфятник - 0\nГалера-Конкистадоров - 0\nФрегат-Конкистадоров - 0\nЛинкор-Конкистадоров - 0\nТяжёлый-Верфятник - 0\n\"Погибель\" - 0\n\"Корсар\" - 0\n\"Бомбандир\" - 0\n\"Браконьер\" - 0\n★Серая-Шляпа★ - 0\n★Красный-Шарф★ - 0\n★Чёрная-Перчатка★ - 0\n★Синий-Сапог★ - 0\nСтаниця - 0\nНаучное-судно - 0\nВахтер - 0\nСолярист - 0\n★Отцовский-Корабль★ - 0\n'+
            f'ДОБЫЧА\n{res["zelezo"]}В-ХОД - 0\n{res["zest"]}В-ХОД - 0\n{res["titan"]}В-ХОД - 0\n{res["vjoblost"]}В-ХОД - 0\n{res["gugol"]}В-ХОД - 0\n{res["gas"]}В-ХОД - 0\n{res["energy"]}В-ХОД - 0\n{res["kamen1"]}В-ХОД - 0\n{res["kamen2"]}В-ХОД - 0\n{res["kamen3"]}В-ХОД - 0\n{res["kamen4"]}В-ХОД - 0\n{res["sverol"]}В-ХОД - 0\n{res["relik"]}В-ХОД - 0\n{res["voda"]}В-ХОД - 0\n{res["naselenie"]}В-ХОД - 0\n{res["mikrobot"]}В-ХОД - 0\n{res["moh"]}В-ХОД - 0\n{res["sol"]}В-ХОД - 0\n{res["antipizdec"]}В-ХОД - 0\n{res["nanohujna"]}В-ХОД - 0\n'+
            f'В-ПРОЦЕССЕ\n')
    with codecs.open(f'UsersData/{user}/общий.txt', 'w', 'utf-8') as f:
        f.write(f'РАСА - КОНКИСТАДОРЫ\nХОД - 0\nПЛАНЕТА - all\nСКЛАД\n{res["zelezo"]} - 0\n{res["zest"]} - 1000\n{res["titan"]} - 0\n{res["vjoblost"]} - 0\n{res["gugol"]} - 0\n{res["gas"]} - 0\n{res["energy"]} - 0\n{res["kamen1"]} - 0\n{res["kamen2"]} - 0\n{res["kamen3"]} - 0\n{res["kamen4"]} - 0\n{res["sverol"]} - 0\n{res["relik"]} - 0\n{res["voda"]} - 0\n{res["naselenie"]} - 0\n{res["mikrobot"]} - 0\n{res["moh"]} - 0\n{res["sol"]} - 0\n{res["antipizdec"]} - 0\n{res["nanohujna"]} - 0\n'+
            f'КОРАБЛИ\nМусорщик - 1\nКаменьщик - 0\nЛегкий-Верфятник - 0\nИстребитель-Капля - 0\nКаравелла - 0\nСредний-Верфятник - 0\nГалера-Конкистадоров - 0\nФрегат-Конкистадоров - 0\nЛинкор-Конкистадоров - 0\nТяжёлый-Верфятник - 0\n\"Погибель\" - 0\n\"Корсар\" - 0\n\"Бомбандир\" - 0\n\"Браконьер\" - 0\n★Серая-Шляпа★ - 0\n★Красный-Шарф★ - 0\n★Чёрная-Перчатка★ - 0\n★Синий-Сапог★ - 0\nСтаниця - 0\nНаучное-судно - 0\nВахтер - 0\nСолярист - 0\n★Отцовский-Корабль★ - 1\n'+
            f'ДОБЫЧА\n{res["zelezo"]}В-ХОД - 0\n{res["zest"]}В-ХОД - 0\n{res["titan"]}В-ХОД - 0\n{res["vjoblost"]}В-ХОД - 0\n{res["gugol"]}В-ХОД - 0\n{res["gas"]}В-ХОД - 0\n{res["energy"]}В-ХОД - 0\n{res["kamen1"]}В-ХОД - 0\n{res["kamen2"]}В-ХОД - 0\n{res["kamen3"]}В-ХОД - 0\n{res["kamen4"]}В-ХОД - 0\n{res["sverol"]}В-ХОД - 0\n{res["relik"]}В-ХОД - 0\n{res["voda"]}В-ХОД - 0\n{res["naselenie"]}В-ХОД - 0\n{res["mikrobot"]}В-ХОД - 0\n{res["moh"]}В-ХОД - 0\n{res["sol"]}В-ХОД - 0\n{res["antipizdec"]}В-ХОД - 0\n{res["nanohujna"]}В-ХОД - 0\n'+
            f'В-ПРОЦЕССЕ\n')
    with codecs.open(f'UsersData/{user}/исследования.txt', 'w', 'utf-8') as f:
        f.write(f'**НАЗЕМНЫЕ ВОЙСКА**\nДжетпак 0\nФаерфлай 0\nСтервятник 0\nАспид 0\nГоняло 0\nМортира 0\nАрбалеста 0\nЯхта 0\nЛат 0\n**ОРУЖИЕ**\nКинетические-ядра 1\nЗаряженные-ядра 0\nПлазменные-ядра 0\nНейтронные-ядра 0\nЖёлтый-луч 1\nАлый-луч 0\nТёмный-луч 0\n**ЗАЩИТА**\nОбычная-броня 1\nЗаряженная-броня 0\nАлая-броня 0\nТёмная-броня 0\nГрави-броня 0\n**ПЕРЕМЕЩЕНИЕ**\nЗвёздные-паруса 1\nАлые-паруса 0\nТёмные-паруса 0\nДвигатель-\"Тёмной-энергии\" 0\n**СПЕЦИАЛИЗИРОВАННЫЕ**\nТранспортный-канал 0\nУбежище 0\nТранспортные-кольца 0\nНасморк 0\nТугие-сплавы 0\n**★Солнечная-Эра★ 0**\n**КАПИТАНСКИЕ**\n**★Серая Шляпа★**\nКаменистые 0\nВторой-слой 0\nПриродные-способности 0\n**★Красный Шарф★**\nАлые 0\nЛучевая-болезнь 0\nИмпульсивная-броня 0\nАлое-пламя 0\nАлые-ками 0\n**★Чёрная Перчатка★**\nТёмные 0\nЧёрная-метка 0\nВылазка 0\nПроникновение 0\nТёмные-силы 0\n**★Синий Сапог★**\nСиние 0\nСиний-луч 0\nСовмещение 0\nКарабины 0\nНовые-гранаты 0')

    #записываем челика в список зареганых
    with codecs.open('UsersData/RegistredPlayers.txt', 'w', 'utf-8') as file_object:
        file_object.write(f'{user}{newL}{contents}')
    