# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
good = False

while not good:
    good = True

    ip = input('Введите IP адрес: ')
    ip = ip.split('.')

    if len(ip) == 4:
        for i in range(4):
            if ip[i].isnumeric():
                ip[i] = int(ip[i])
                if (ip[i] < 0 or ip[i] > 255):
                    good = False
            else:
                good = False
    else:
        good = False
    if not good:
        print('Неправильный IP-адрес')
    else:
        if ((ip[0] >= 1) and (ip[0] <= 223)):
            print('unicast')
        elif ((ip[0] >= 224) and (ip[0] <= 239)):
            print('multicast')
        elif (ip[0] == ip[1] == ip[2] == ip[3] == 255):
            print('local broadcast')
        elif (ip[0] == ip[1] == ip[2] == ip[3] == 0):
            print('unasigned')
        else:
            print('unused')
