# -*- coding: utf-8 -*-

"""
Задание 23.3

Скопировать и изменить класс Topology из задания 22.1x.

Добавить метод, который позволит выполнять сложение двух экземпляров класса Topology.
В результате сложения должен возвращаться новый экземпляр класса Topology.

Создание двух топологий:

In [1]: t1 = Topology(topology_example)

In [2]: t1.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [3]: topology_example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
                             ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

In [4]: t2 = Topology(topology_example2)

In [5]: t2.topology
Out[5]: {('R1', 'Eth0/4'): ('R7', 'Eth0/0'), ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

Суммирование топологий:

In [6]: t3 = t1+t2

In [7]: t3.topology
Out[7]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R1', 'Eth0/6'): ('R9', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Проверка, что исходные топологии не изменились:

In [9]: t1.topology
Out[9]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [10]: t2.topology
Out[10]: {('R1', 'Eth0/4'): ('R7', 'Eth0/0'), ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}
"""

topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}

topology_example2 = {
    ("R1", "Eth0/4"): ("R7", "Eth0/0"),
    ("R1", "Eth0/6"): ("R9", "Eth0/0"),
}


class Topology:

    def _normalize(self, topology_dict):
        temp_topo = dict()
        for link in topology_dict:
            if link > topology_dict[link]:
                temp_topo[topology_dict[link]] = link
            else:
                temp_topo[link] = topology_dict[link]
        return temp_topo

    def delete_link(self, key1, key2):
        if self.topology.get(key1):
            del self.topology[key1]
        elif self.topology.get(key2):
            del self.topology[key2]
        else:
            print('Такого соединения нет')

    def delete_node(self, node):
        del_nodes = []
        for link in self.topology:
            if (link[0] == node) | (self.topology[link][0] == node):
                del_nodes.append(link)
        if del_nodes:
            for node in del_nodes:
                del self.topology[node]
        else:
            print('Такого устройства нет')

    def add_link(self, side1, side2):
        one_side = False
        link_present = False
        for link in self.topology:
            if ((link == side1) and (self.topology[link] == side2)) or ((link == side2) and (self.topology[link] == side1)):
                link_present = True
            elif (link == side1) or (self.topology[link] == side2) or (link == side2) or (self.topology[link] == side1):
                one_side = True
        if link_present:
            print('Такое соединение существует')
        elif one_side:
            print('Cоединение с одним из портов существует')
        else:
            self.topology[side1] = side2

    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def __add__(self, t2):
        temp_topo = t2.topology
        for link in temp_topo:
            self.topology[link] = temp_topo[link]
        return self.topology

if __name__ == '__main__':
    t1 = Topology(topology_example)
    t2 = Topology(topology_example2)
    t3 = t1 + t2
    print(t3)