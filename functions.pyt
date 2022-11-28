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