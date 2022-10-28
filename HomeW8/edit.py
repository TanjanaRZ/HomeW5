import row
import add

def editUser(users, num):
    men = '''Что редактировать:
    i - id;
    fn - Имя;
    sn - Фамилия;
    d - Дата рождения;
    dp - Отдел;
    fp - Личный номер;
    sp - Рабочий номер; 
    ex - выход'''
    print(men)
    chos(users, num)
    

def chos(users, num):
    secs = '''
    Изменено
'''
    secs = '─'*100 + secs + '─'*100
    ans = input('Ответ: ')
    if ans == 'i':
        users[num][0] = add.check('id (5 цифр, ex - выход): ','[0-9]{5}',users)
        print(secs)
    elif ans == 'fn':
        users[num][1] = add.check('Имя (ex - выход): ','[а-яА-Я]{2,10}',users)
        print(secs)
    elif ans == 'sn':
        users[num][2] = add.check('Фамилия (ex - выход): ','[а-яА-Я]{2,12}',users)
        print(secs)
    elif ans == 'd':
        users[num][3] = add.check('Дата рождения (**.**.****, ex - выход): ','[0-9]{1,2}.[0-9]{1,2}.[0-9]{4}',users)
        print(secs)
    elif ans == 'dp':
        users[num][4] = add.check('Отдел: (ex - выход)','[а-яА-Я]{2,12}',users)
        print(secs)
    elif ans == 'fp':
        users[num][5] = add.check('Личный номер (+7 *** *** **-**, ex - выход): ','\+7 [0-9]{3} [0-9]{3} [0-9]{2}-[0-9]{2}',users)
        print(secs)
    elif ans == 'sp':
        users[num][6] = add.check('Рабочий номер (+7 *** *** **-** или пусто, ex - выход): ','\+7 [0-9]{3} [0-9]{3} [0-9]{2}-[0-9]{2}|',users)
        print(secs) 
    elif ans == 'ex':
        print('─'*100)
        row.showUser(users, num)
    else:
        print('─'*100)
        print('Введите корректный код')
        print('─'*100)
    editUser(users, num)