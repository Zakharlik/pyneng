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
output = '{:25} {}\n' * 6

with open('ospf.txt','r') as infile:
    for line in infile:
            proto, prefix, ad, _, nexthop, lastupd, iface = line.split()
            if proto == 'O':
                proto = 'OSPF'
            elif proto == 'I':
                proto == 'IGRP'
            print('-'*44)
            print(output.format(
                "Protocol:",proto,
                "Prefix:",prefix,
                "AD/Metric:",ad[1:-1],
                "Next-Hop:",nexthop[:-1],
                "Last update:",lastupd[:-1],
                "Outbound Interface",iface))