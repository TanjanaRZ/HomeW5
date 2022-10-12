# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг 
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не 
# более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего 
# конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


import random

def howRock(rocks, maxRock):
    if rocks <= maxRock:
        return rocks
    elif (rocks % maxRock) <= 0:
        return maxRock - 1
    else:
        return (rocks % maxRock - 1)

rocks = 200
maxRock = 28
hod = random.randint(0, 1)

while rocks > 0:
    if hod == 0:
        tc = howRock(rocks, maxRock)
        rocks = rocks - tc
        print("Бот взял " + str(tc) + ", осталось: " + str(rocks))
        hod = 1
    elif hod == 1:
        pltc = int(input("Сколько? "))
        if pltc > 0 and pltc <= 28:
            rocks = rocks - pltc
            print("Игрок взял " + str(pltc) + ", осталось: " + str(rocks))
            hod = 0
        else:
            print("Введите корректное значение")
    if rocks <= 0:
        if hod == 0:
            print("Победил игрок")
        elif hod == 1:
            print("Победил бот")