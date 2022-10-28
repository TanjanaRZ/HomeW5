import csv

def load():
    lst = []
    with open("C:\\Users\\1\\Desktop\\учеба\\Python\\Домашние задания\\Home\\HomeW8\\users.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            lst.append(row)
    print('─'*100)
    print('Список загружен')
    print('─'*100)
    f.close()
    return lst
    
def save(users):
    if len(users) == 0:
        print('Нечего сохранять')
    else:
        with open("C:\\Users\\1\\Desktop\\учеба\\Python\\Домашние задания\\Home\\HomeW8\\users.csv", 'w') as f:
            writer = csv.writer(f, lineterminator="\r")
            for i in range(len(users)):
                
                writer.writerow(users[i])
        print('─'*100)
        print('Список сохранён')
        print('─'*100)
        f.close()