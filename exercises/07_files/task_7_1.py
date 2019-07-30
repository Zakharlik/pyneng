# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


with open('ospf.txt','r') as infile:
    for line in infile:
            proto, prefix, ad, _, nexthop, lastupd, iface = line.split()
            if proto == 'O':
                proto = 'OSPF'
            elif proto == 'I':
                proto == 'IGRP'
            print('-'*44)
            print('{:22} {:22}'.format("Protocol:",proto))
            print('{:22} {:22}'.format("Prefix:",prefix))
            print('{:22} {:22}'.format("AD/Metric:",ad[1:-1]))
            print('{:22} {:22}'.format("Next-Hop:",nexthop[:-1]))
            print('{:22} {:22}'.format("Last update:",lastupd[:-1]))
            print('{:22} {:22}'.format("Outbound Interface",iface))
