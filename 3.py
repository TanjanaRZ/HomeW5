# Создайте программу для игры в ""Крестики-нолики"".

import random

def showFld (lst):
    print ('  1 2 3')
    print ('1 ' + lst[0][0] + ' ' + lst[0][1] + ' ' + lst[0][2])
    print ('2 ' + lst[1][0] + ' ' + lst[1][1] + ' ' + lst[1][2])
    print ('3 ' + lst[2][0] + ' ' + lst[2][1] + ' ' + lst[2][2])
    
def setCell (lst, crd, unt):
    rw = int(crd[0]) - 1
    clm = int(crd[1]) - 1
    if rw >= 0 and rw <= 2 and clm >= 0 and clm <= 2 and lst[rw][clm] == '*':
        lst[rw][clm] = unt
        return True
    else:
        print("Введите корректные координаты")
        return False

def whoWin (lst):
    res = ""
    if lst[0][0] == lst[1][1] and lst[2][2] == lst[0][0] and lst[0][0] != '*':
        res =  lst[0][0]
    elif lst[0][2] == lst[1][1] and lst[2][0] == lst[0][2] and lst[0][2] != '*':
        res =  lst[0][2]
    for i in range(3):
        if lst[0][i] == lst[1][i] and lst[2][i] == lst[0][i] and lst[0][i] != '*':
            res =  lst[0][i]
        elif lst[i][0] == lst[i][1] and lst[i][2] == lst[i][0] and lst[i][0] != '*':
            res =  lst[i][0]
    return res



fld = [["*", "*", "*"],["*", "*", "*"],["*", "*", "*"]]
hod = random.randint(0, 1)
cnt = ''

showFld(fld)
while cnt == '':
    if hod == 1:
        cell = input("Ход игрока 0 (Введите номер строки и столбца без пробела): ")
        if setCell(fld, cell, "0"):
            showFld(fld)
            hod = 0
    else:
        cell = input("Ход игрока X (Введите номер строки и столбца без пробела): ")
        if setCell(fld, cell, "X"):
            showFld(fld)
            hod = 1
    cnt = whoWin(fld)

if cnt == '0':
    print("Победил игрок 0")
else:
    print("Победил игрок X")

