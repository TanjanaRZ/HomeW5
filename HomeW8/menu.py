import fl
import shlst

def show(users):
    menu = '''Выбирете действие:
 l - Загрузить список;
 sv - Сохранить список;
 sh - Показать список;
 ex - Выход'''
    print(menu)
    qwst(users)

def qwst(users):
    ans = input('Ответ: ')
    if ans == 'l':
        users = fl.load()
    elif ans == 'sv':
        fl.save(users)
    elif ans == 'sh':
        shlst.openMenu(users)
    elif ans == 'ex':
        print('─'*100)
        exit(0)
    else:
        print('─'*100)
        print('Введите корректный код')
        print('─'*100)
    qwst(users)