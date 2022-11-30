from data import tanks,löveg,országok
from os import system
def menu():
    system('cls')
    print('0 - Kilépés')
    print('1 - Vissza')
    print('2 - Lista elemeinek száma')
    print('3 - Lista x. elemének megjelenítése')
    print('4 - Elen hozzáadása a listához')
    print('5 - Elem törlése a listából')
    print('6 - Löveggel kompatibilis tankok')
    print('7 - Tank származási helye')
    print('8 - Hány tank származik a bizonyos országból')
    return input('Válasszon a menüpontok közül!')

def fajlBeolvasas():
    file=open('jumps.csv','r',encoding='utf-8')
    file.readline()
    for egysor in file:
        darabolt=egysor.strip().split(';')
        tanks.append(darabolt[0])
        országok.append(float(darabolt[1]))
        országok.append(float(darabolt[1]))
    file.close()

def kiÍr():
    system('cls')
    print('-----Tankok-----\n')
    for tank in tanks:
        print(f'\t{tank}')
    input()
