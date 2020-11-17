# -*- coding: utf-8 -*-
"""
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
"""
import argparse
import subprocess
import ipaddress
import tabulate


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


def ping_ip_addresses(ip_list):
    good_ip = []
    bad_ip = []
    for ip in ip_list:
        print(f'Pinging: {ip} ', end = '', flush = True)
        reply = subprocess.run(['ping', '-c', '1', '-n', ip],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
        if reply.returncode == 0:
            print('Ok')
            good_ip.append(ip)
        else:
            print('No reply')
            bad_ip.append(ip)
    return (good_ip, bad_ip)
    
def print_ip_table(ip_list):
    table = ping_ip_addresses(convert_ranges_to_ip_list(ip_list))
    print(table[0])
    print('-'*10)
    print(table[1])
    dict_table ={'Reachable': table[0], 'Unreachable': table[1]}
    print(tabulate(dict_table))
    
if __name__ == '__main__':
    print_ip_table(['10.40.1.1', '10.40.2.1-10', '10.40.0.20-10.40.0.25'])
