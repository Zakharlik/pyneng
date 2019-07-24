#!/usr/bin/env python
from sys import argv

template = '''
Network:
{0:<9}{1:<9}{2:<9}{3:<9}
{0:<08b} {1:<08b} {2:<08b} {3:<08b}

Mask:
/{4}
{5:<9}{6:<9}{7:<9}{8:<9}
{5:<08b} {6:<08b} {7:<08b} {8:<08b}
'''	
		   

#ip = input('IP/mask: ')
#ip,mask = ip.split('/')
ip = str(argv[1])
mask = int (argv[2])
ip = ip.split('.')
#mask=int(mask)
bitip=(((int(ip[0])*256+int(ip[1]))*256+int(ip[2]))*256+int(ip[3]))
bitip=bin(bitip)[2:]
bitip='0'*(32-len(bitip))+bitip 

bitip=bitip[:('1'*mask+'0'*(32-mask)).find('0')]+'0'*(32-(('1'*mask+'0'*(32-mask)).find('0'))) 


print(template.format(int(int(int(int(bitip,2)/256)/256)/256),
 int(int(int(bitip,2)/256)/256)%256, 
 int(int(bitip,2)/256)%256, 
 int(bitip,2)%256,
 mask,
 int(int(int(int('1'*mask+'0'*(32-mask),2)/256)/256)/256),
 int(int(int('1'*mask+'0'*(32-mask),2)/256)/256)%256, 
 int(int('1'*mask+'0'*(32-mask),2)/256)%256, 
 int('1'*mask+'0'*(32-mask),2)%256))
  
  
