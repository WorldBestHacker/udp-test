#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import pickle
import os
import sys
sys.path.append("EduBot/EduBotLibrary")
import edubot


#IP = "127.0.0.1"
IP = str(os.popen("hostname -I | cut -d\" \" -f1").readline().replace("\n",""))
PORT = 8000
TIMEOUT = 60 #время ожидания приема сообщения

def motorRun(leftSpeed, rightSpeed):
    robot.leftmotor.SetSpeed(leftSpeed)
    robot.rightmotor.SetSpeed(rightSpeed)

def beep():
    print("Beep!!!")
    robot.Beep()
def Exit():
    print("exit")
    running = False

robot = edubot.EduBot(1)
assert robot.Check(), 'EduBot not found!!!'
robot.Start() #обязательная процедура, запуск потока отправляющего на контроллер EduBot онлайн сообщений
print ('EduBot started!!!')

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
    
    if data:
        msg = "message recieved"
        server.sendto(msg.encode("utf-8"), adrs) #отправляем ответ (msg)
        
    cmd, param = pickle.loads(data[0]) #распаковываем полученное сообщение
    leftSpeed, rightSpeed = param
    adrs = data[1] #адрес, с которого было отправлено сообщение

    print(cmd, param, adrs)

    if(cmd == "speed"):
        print("leftSpeed: %d, rightSpeed: %d" % (leftSpeed, rightSpeed))
        motorRun(leftSpeed, rightSpeed)
    elif(cmd == "beep"):
        beep()
    elif cmd == "exit":
        Exit()
    elif:
        print("Unknown command: %s" % cmd)
        
    
motorRun(0, 0)
robot.Release()
server.close()
print("End program")
