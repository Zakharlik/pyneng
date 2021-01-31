# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re


def parse_sh_cdp_neighbors(sh_cdp_ne):
    neighbors_dict = {}
    neighbors_list = {}
    sh_cdp_ne = sh_cdp_ne.split('\n')
    for line in sh_cdp_ne:
        if '>' in line:
            hostname = re.search('^(\S+)>',line).group(1)
            neighbors_dict[hostname] = ''
        if not 'Port' in line:
            match = re.search('(?P<device>\S+)\s+(?P<local_if>\S+\s\S+)\s+\S+\S+[\S\s]+\s+\d+\s+(?P<rem_if>\S+\s\S+)',line)
        if match:
            neighbors_list[match.group('local_if')] = {match.group('device') : match.group('rem_if')}
#            print(neighbors_list)
    neighbors_dict[hostname] = neighbors_list
    return neighbors_dict

if __name__ == '__main__':
    with open('sh_cdp_n_sw1.txt') as f:
        print(parse_sh_cdp_neighbors(f.read()))