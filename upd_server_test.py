#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import pickle

IP = '127.0.0.1'
PORT = 8000
TIMEOUT = 60 #время ожидания приема сообщения

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #создаем сервер
server.bind((IP, PORT)) #запускаем сервер
print("Listening %s on port %d..." % (IP, PORT)) #выводим сообщение о запуске сервера
server.settimeout(TIMEOUT) #указываем серверу время ожидания приема сообщения

running = True

while running:
    try:
        data = server.recvfrom(1024) #пытаемся получить данные
    except socket.timeout: #если вышло время, то выходим из цикла
        print("Time is out...")
        break
      
    cmd, param = pickle.loads(data[0]) #распаковываем полученное сообщение 
    adrs = data[1] #адрес, с которого было отправлено сообщение

    print(cmd, param, adrs)

        
    #msg = 'Ok'
    #server.sendto(msg.encode('utf-8'), adrs) #отправляем ответ (msg)
        
server.close()
