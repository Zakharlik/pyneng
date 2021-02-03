# -*- coding: utf-8 -*-
"""
Задание 17.3b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует функция draw_topology из файла draw_network_graph.py).

Проверить работу функции на файле topology.yaml (должен быть создан в задании 17.3a).
На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology из файла draw_network_graph.py.

Результат должен выглядеть так же, как схема в файле task_17_3b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""

import draw_network_graph
import yaml

def transform_topology(yaml_file_name):
    topology_dict = {}
    with open(yaml_file_name, 'r') as f:
        sh_ne_dict = yaml.safe_load(f)
    for host_a in sh_ne_dict:
        for port_a in sh_ne_dict[host_a]:
            for host_b in sh_ne_dict[host_a][port_a]:
                port_b = sh_ne_dict[host_a][port_a][host_b]
                if host_a < host_b:
                    topology_dict[(host_a, port_a)] = (host_b, port_b)
                else:
                    topology_dict[(host_b, port_b)] = (host_a, port_a)
    return topology_dict


if __name__ == '__main__':
    draw_network_graph.draw_topology(transform_topology('topology.yaml'))

