#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']


fname = argv[1]
outfile = open('config_sw1_cleared.txt', 'w')

with open(fname, 'r') as fil:
    for line in fil:
        prt = True
        for i in range(len(ignore)):
            if line.find(ignore[i]) >= 0:
                prt = False
        if prt:
            outfile.write(line)


'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
