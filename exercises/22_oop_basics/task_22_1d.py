# -*- coding: utf-8 -*-

"""
Задание 22.1d

Изменить класс Topology из задания 22.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще
 нет в топологии.
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение
"Cоединение с одним из портов существует"


Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Cоединение с одним из портов существует


"""


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


if __name__ == '__main__':
    top = Topology(topology_example)
    top.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    top.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    top.add_link(('R1', 'Eth0/4'), ('R5', 'Eth5/0'))
