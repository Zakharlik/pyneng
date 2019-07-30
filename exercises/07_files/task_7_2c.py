#!/usr/bin/env python
# -*- coding: utf-8 -*-

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

fname = argv[1]
outfile = open(argv[2],'w')

with open(fname,'r') as fil:
    for line in fil:
#        if not line.startswith('!'):
#            if not set(ignore).intersection(set(line.split())):
            prt = True
            for i in range(len(ignore)):
                if line.find(ignore[i]) >= 0:
                    prt = False
            if prt:
#                print(line.strip())
                outfile.write(line)


'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
