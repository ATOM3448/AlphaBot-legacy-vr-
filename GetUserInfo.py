import asyncio
import json
import codecs
import os
import discord
from FMFresurses import res

#Получить файл
def getLineInFile(user_id, file):
    lineInFile = []
    with codecs.open(f'UsersData/{user_id}/{file}.txt', 'r+', 'utf-8') as _file:
        count = 0
        while True:
            lineInFile.append(_file.readline())
            if not lineInFile[count]:
                break
            count += 1
    return lineInFile

#Получить расу
def getRace(user_id, file = 'общий'):
    lineInFile = getLineInFile(user_id, file)
    race = ''
    for i in lineInFile:
        if(i[0] != 'Р'):
            continue
        if(i[0] + i[1] + i[2] + i[3] == 'РАСА' ):
            count = 0
            for ii in i:
                if(ii == ' '):
                    count = 1
                if(count == 1):
                    if((ii != ' ') and (ii != '-')):
                        race+=ii
            break
    return race

#Получить актуальный ход
def getTurn(user_id, file = 'общий'):
    lineInFile = getLineInFile(user_id, file)
    turn = ''
    for i in lineInFile:
        if(i[0] != 'Х'):
            continue
        if(i[0] + i[1] + i[2] == 'ХОД' ):
            count = 0
            for ii in i:
                if(ii == ' '):
                    count = 1
                if(count == 1):
                    if((ii != ' ') and (ii != '-')):
                        turn+=ii
            break
    return turn

#Получить планету
def getPlaneti(user_id, file = 'общий'):
    lineInFile = getLineInFile(user_id, file)
    planeti = ''
    for i in lineInFile:
        if(i[0] != 'П'):
            continue
        if(i[0] + i[1] + i[2] + i[3] + i[4] + i[5] + i[6] == 'ПЛАНЕТА' ):
            count = 0
            for ii in i:
                if(ii == ' '):
                    count = 1
                if(count == 1):
                    if((ii != ' ') and (ii != '-')):
                        planeti+=ii
            break
    return planeti

#Получить полный склад
def getCargoFull(user_id, file = 'общий'):
    lineInFile = getLineInFile(user_id, file)
    cargo = ''
    check = 0
    for i in lineInFile:
        if(i[0] == 'С'):
            check += 1
        if(check == 1):
            if(i[0]+i[1]+i[2]+i[3]+i[4] == 'СКЛАД'):
                check += 1
            else:
                check = 0
        if(check == 2):
            if((i[0] != 'С') and (i[0] != '<')):
                check+=1
        if(check == 3):
            break
        if((check == 2) and (i[0] != 'С')):
            cargo+=i
    return cargo
#Получить склад без нулей