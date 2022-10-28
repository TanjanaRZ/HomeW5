import table
import shlst
import edit

def showUser(users, num):
    table.showTop()
    print(table.crRow(users[num], num))
    ln = '''───┴─────┴──────────┴────────────┴──────────┴────────────┴────────────────┴────────────────'''
    print(ln)
    menuUser(users, num)
    
    
def menuUser(users, num):
    men = '''Выбирете действие:
 e - Редактировать контакт;
 d - Удалить контакт;
 ex - назад'''
    print(men)
    chos(users, num)
    

def chos(users, num):
    ans = input('Ответ: ')
    if ans == 'e':
        edit.editUser(users, num)
    elif ans == 'd':
        users.pop(num)
        print('─'*100)
        print('Контакт удалён')
        print('─'*100)
        shlst.openMenu(users)
    elif ans == 'ex':
        print('─'*100)
        shlst.openMenu(users)
    else:
        print('─'*100)
        print('Введите корректный код')
        print('─'*100)
    chos(users, num)