#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

fname = argv[1]

with open(fname,'r') as fil:
    for line in fil:
        if not line.startswith('!'):
#            if not set(ignore).intersection(set(line.split())):
            prt = True
            for i in range(len(ignore)):
                if line.find(ignore[i]) >= 0:
                    prt = False
            if prt:
                print(line.strip())
