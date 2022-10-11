# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


import re

txt = "Пример использования всех основных функций абв"

wrd = txt.split(" ")

for i in range(len(wrd)):
    if re.fullmatch(r".*абв.*",wrd[i]):
        wrd.pop(i)
        
print(wrd)


