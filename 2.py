# Дана последовательность чисел. Получить список уникальных элементов заданной
#  последовательности, список повторяемых и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]


orgn = [1, 2, 3, 5, 1, 5, 3, 10]
pov = [1]
unq = [orgn[0]]


for i in range(1, len(orgn)):
    unqbl = True
    for j in range(len(unq)):
        if orgn[i] == unq[j]:
            pov[j] += 1
            unqbl = False
            
    if unqbl:
        unq.append(orgn[i])
        pov.append(1)

one = []
much = []

for i in range(len(unq)):
    if pov[i] == 1:
        one.append(unq[i])
    else:
        much.append(unq[i])

print(unq)
print(one)
print(much)
