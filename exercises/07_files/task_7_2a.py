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

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']


fname = argv[1]

with open(fname, 'r') as fil:
    for line in fil:
        if not line.startswith('!'):
            prt = True
            for ignore_word in ignore:
                if ignore_word in line:
                    prt = False
                    break
            if prt:
                print(line.rstrip())
