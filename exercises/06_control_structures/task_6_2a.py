# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ip = input('Введите IP адрес: ')

ip = ip.split('.')
good = True

if len(ip) == 4:
    for i in range(4):
        if ip[i].isnumeric():
            ip[i]=int(ip[i])
            if (ip[i] <0 or ip[i] >255):
                good = False
        else:
            good = False
else:
    good = False
if not good:
    print('Неправильный IP-адрес')        
else:   
    if ((ip[0] >=1) and (ip[0]<=223)):
        print('unicast')
    elif ((ip[0] >=224) and (ip[0]<=239)):
        print('multicast')
    elif (ip[0] == ip[1] == ip[2] == ip[3] == 255):
        print('local broadcast')
    elif (ip[0] == ip[1] == ip[2] == ip[3] == 0):
        print('unasigned')
    else:
        print('unused')
        
