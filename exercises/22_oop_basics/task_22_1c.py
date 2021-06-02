# -*- coding: utf-8 -*-

"""
Задание 22.1c

Изменить класс Topology из задания 22.1b.

Добавить метод delete_node, который удаляет все соединения с указаным устройством.

Если такого устройства нет, выводится сообщение "Такого устройства нет".

Создание топологии
In [1]: t = Topology(topology_example)

In [2]: t.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление устройства:
In [3]: t.delete_node('SW1')

In [4]: t.topology
Out[4]:
{('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Если такого устройства нет, выводится сообщение:
In [5]: t.delete_node('SW1')
Такого устройства нет

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
    print(top.topology)
    top.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))
    print(top.topology)
    top.delete_node('SW1')
    print(top.topology)
    top.delete_node('SW1')
   
