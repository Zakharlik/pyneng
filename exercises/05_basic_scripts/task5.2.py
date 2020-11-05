#!/usr/bin/env python
template = '''
Network:
{0:<9}{1:<9}{2:<9}{3:<9}
{0:<08b} {1:<08b} {2:<08b} {3:<08b}

Mask:
/{4}
{5:<9}{6:<9}{7:<9}{8:<9}
{5:<08b} {6:<08b} {7:<08b} {8:<08b}
'''	
		   

ip = input('IP/mask: ')
ip,mask = ip.split('/')
ip = ip.split('.')
print(template.format(int(ip[0]),
 int(ip[1]),
 int(ip[2]),
 int(ip[3]),
 mask,
 int(int(int(int('1'*int(mask)+'0'*(32-int(mask)),2)/256)/256)/256),
 int(int(int('1'*int(mask)+'0'*(32-int(mask)),2)/256)/256)%256, 
 int(int('1'*int(mask)+'0'*(32-int(mask)),2)/256)%256, 
 int('1'*int(mask)+'0'*(32-int(mask)),2)%256))
  
  
