#!/usr/bin/env python
# -*- coding: utf-8 -*-
vlans =dict()
with open('CAM_table.txt','r') as fil:
    for line in fil:
        if (line.startswith(' ') and line[1]!=' '):
            vlan, mac, _, port = line.split()        
            vlans.update({vlan: [mac,port]})
vlan_list = sorted(vlans)
for vlan in vlan_list:
    print('{:5}{:20}{:10}'.format(vlan, vlans[vlan][0],vlans[vlan][1]))
