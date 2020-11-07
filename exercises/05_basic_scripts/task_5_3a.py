#!/usr/bin/env python
from sys import argv


access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]
access_template = '\n'.join(access_template)

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
trunk_template = '\n'.join(trunk_template)

question = {'access': 'Введите номер VLAN:', 'trunk': 'Введите разрешенные VLANы:'}


template = {'access': access_template, 'trunk': trunk_template}
inttype = input ('Введите режим работы интерфейса (access/trunk): ')
intnum = input ('Введите тип и номер интерфейса: ')
vlans = input(question[inttype])

print('interface {}'.format(intnum))
print(template[inttype].format(vlans))
