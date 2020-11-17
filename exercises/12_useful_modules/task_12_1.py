# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import argparse
import subprocess

def ping_ip_addresses(ip_list):
    good_ip = []
    bad_ip = []
    for ip in ip_list:
        reply = subprocess.run(['ping', '-c', '1', '-n', ip],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
        if reply.returncode == 0:
            good_ip.append(ip)
        else:
            bad_ip.append(ip)
    return (good_ip, bad_ip)


parser = argparse.ArgumentParser(description='Ping script')

parser.add_argument('ips', nargs='+', help='IP adresses')
args = parser.parse_args()
ping_result = ping_ip_addresses(args.ips)
print(ping_result)
