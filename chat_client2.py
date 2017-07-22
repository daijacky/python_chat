# coding:utf-8
 
#  __author__ = 'Mark sinoberg'
#  __date__ = '2016/7/7'
#  __Desc__ = socket的客户端的简单实现
 
import socket
 
PORT = 9998
HOST = '127.0.0.1'
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9697))
words = raw_input('Client2:')
while words != 'quit':
  s.sendto(words,(HOST,PORT))
  words = raw_input('Client2:')
while True:
    data,addr = s.recvfrom(1024)
    print data
s.close()