# -*- coding: utf-8 -*-

"""
Задание 23.1a

Скопировать и изменить класс IPAddress из задания 23.1.

Добавить два строковых представления для экземпляров класса IPAddress.
Как дожны выглядеть строковые представления, надо определить из вывода ниже:

Создание экземпляра
In [5]: ip1 = IPAddress('10.1.1.1/24')

In [6]: str(ip1)
Out[6]: 'IP address 10.1.1.1/24'

In [7]: print(ip1)
IP address 10.1.1.1/24

In [8]: ip1
Out[8]: IPAddress('10.1.1.1/24')

In [9]: ip_list = []

In [10]: ip_list.append(ip1)

In [11]: ip_list
Out[11]: [IPAddress('10.1.1.1/24')]

In [12]: print(ip_list)
[IPAddress('10.1.1.1/24')]

"""
class IPAddres:
  def isIpCorrct(self, ipAddress):
    octets = ipAddress.split('.')
    isIpCorrect = True;
    if len(octets) == 4:
      for octet in octets:
        try:
          if int(octet) < 0 or int(octet) > 255:
            isIpCorrect = False
        except ValueError:
          raise ValueError('Incorrect IPv4 address')
    else:
      raise ValueError('Incorrect IPv4 address')
    if not isIpCorrect:
      raise ValueError('Incorrect IPv4 address')
    return True

  def isMaskCorrect(self, mask):
    try:
      if int(mask) < 8 or int(mask) > 24:
        raise ValueError('Incorrect mask')
    except:
      raise ValueError('Incorrect mask')
    print('Mask checked')
    return True

  def isAddressMaskCorrect(self, ipAddressMask):
    self.ip, self.mask = ipAddressMask.split('/')
    if self.isIpCorrct(self.ip) and self.isMaskCorrect(self.mask):
      return True

  def __init__(self, ipAddressMask):
    res = self.isAddressMaskCorrect(ipAddressMask)

  def __str__(self) -> str:
      return f'IP address {self.ip}/{self.mask}'
  
  def __repr__(self) -> str:
      return f"IP address('{self.ip}/{self.mask}')"

if __name__ == "__main__":
  ip1 = IPAddres('100.1.1.1/24')
  print(ip1)
  ip_list = []
  ip_list.append(ip1)
  print(ip_list)
