# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress

def convert_ranges_to_ip_list(ip_list):
    full_ip_list = []
    for ip in ip_list:
        try:
            ipaddress.ip_address(ip)
            full_ip_list.append(ip)
        except ValueError:
            try:
                second_ip = ip.split('-')[1]
                ipaddress.ip_address(ip.split('-')[1])
                ip_head = '.'.join(ip.split('.')[:3])
                ip_start = int(ip.split('-')[0].split('.')[3])
                ip_end =  int(ip.split('-')[1].split('.')[3])
            except ValueError:
                ip_head = '.'.join(ip.split('.')[:3])
                ip_start = int(ip.split('-')[0].split('.')[3])
                ip_end =  int(ip.split('-')[1])
            for ip_tail in range(ip_start, ip_end+1):
                ip = ip_head+'.'+str(ip_tail)
                full_ip_list.append(ip)
    return full_ip_list


print(convert_ranges_to_ip_list(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']))