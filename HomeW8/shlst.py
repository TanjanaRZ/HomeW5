import table
import row
import menu
import add

def openMenu(users):
    if len(users) == 0:
        print('Нечего показывать')
        print('─'*100)
    else:
        men = '''Как показать?
 t - Весь список;
 число - Контакт под номером;
 a - Добавить контакт;
 ex - назад'''
        print(men)
        qwst(users)

def qwst(users):
    ans = input('Ответ: ')
    if ans == 't':
        table.show(users)
    elif ans.isdigit() and int(ans)>0 and int(ans)<len(users):
        row.showUser(users,int(ans))
    elif ans == 'a':
        add.addUser(users)
    elif ans == 'ex':
        print('─'*100)
        menu.show(users)
    else:
        print('─'*100)
        print('Введите корректный код')
        print('─'*100)
    qwst(users)