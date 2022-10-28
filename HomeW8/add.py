import shlst
import re

def addUser(users):
    user = [check('id (5 цифр, ex - выход): ','[0-9]{5}',users)]
    user.append(check('Имя (ex - выход): ','[а-яА-Я]{2,10}',users))
    user.append(check('Фамилия (ex - выход): ','[а-яА-Я]{2,12}',users))
    user.append(check('Дата рождения (**.**.****, ex - выход): ','[0-9]{1,2}.[0-9]{1,2}.[0-9]{4}',users))
    user.append(check('Отдел: (ex - выход)','[а-яА-Я]{2,12}',users))
    user.append(check('Личный номер (+7 *** *** **-**, ex - выход): ','\+7 [0-9]{3} [0-9]{3} [0-9]{2}-[0-9]{2}',users))
    user.append(check('Рабочий номер (+7 *** *** **-** или пусто, ex - выход): ','\+7 [0-9]{3} [0-9]{3} [0-9]{2}-[0-9]{2}|',users))
    users.append(user)
    print('─'*100)
    print('Контакт добавлен')
    print('─'*100)
    shlst.openMenu(users)
    

def check(st, rex, users):
    res = input(st)
    if res == 'ex': 
        shlst.openMenu(users)
    elif re.fullmatch(rex, res) != None:
        return res
    else:
        print('─'*100)
        print('Введите корректный код')
        print('─'*100)
        return check(st, rex, users)