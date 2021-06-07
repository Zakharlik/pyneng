#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
user_vlan = input('Please enter VLAN number:')
user_vlan = int(user_vlan.strip())
with open('CAM_table.txt', 'r') as fil:
    for line in fil:
        if (line.startswith(' ') and line[1] != ' '):
            vlan, mac, _, port = line.split()
            if user_vlan == int(vlan):
                print(f'{vlan:<7}{mac:20}{port:10}')
