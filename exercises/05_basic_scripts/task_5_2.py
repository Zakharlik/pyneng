#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ipmask = input('IP/mask:')
# ipmask = '10.40.1.9/22'
ip_str, mask = ipmask.split('/')

mask_str = '1' * int(mask) + '0' * (32 - int(mask))
mask_bin = [int(mask_str[0:8], 2),
            int(mask_str[8:16], 2),
            int(mask_str[16:24], 2),
            int(mask_str[24:32], 2)]

ip_dec_str = ip_str.split('.')
ip_dec = []
ip_dec.append(int(ip_dec_str[0]))
ip_dec.append(int(ip_dec_str[1]))
ip_dec.append(int(ip_dec_str[2]))
ip_dec.append(int(ip_dec_str[3]))

template = f'''Network:
{ip_dec[0]:<8}  {ip_dec[1]:<8}  {ip_dec[2]:<8}  {ip_dec[3]:<8}
{ip_dec[0]:>08b}  {ip_dec[1]:>08b}  {ip_dec[2]:>08b}  {ip_dec[3]:>08b}

Mask:
/{mask}
{mask_bin[0]:<8}  {mask_bin[1]:<8}  {mask_bin[2]:<8}  {mask_bin[3]:<8}
{mask_bin[0]:08b}  {mask_bin[1]:08b}  {mask_bin[2]:08b}  {mask_bin[3]:08b}
'''

print(template)
