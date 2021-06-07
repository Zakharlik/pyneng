#!/usr/bin/env python
# -*- coding: utf-8 -*-
vlans = []
with open('CAM_table.txt', 'r') as fil:
    for line in fil:
        if (line.startswith(' ') and line[1] != ' '):
            vlan, mac, _, port = line.split()
            vlans.append([int(vlan), mac, port])
vlan_list = sorted(vlans)
for vlan in vlan_list:
    print('{:<7}{:20}{:10}'.format(vlan[0], vlan[1], vlan[2]))
