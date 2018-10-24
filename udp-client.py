#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import pickle
import time
import pygame

def SendCommand(cmd, param = 0):
    """функция, запаковывающая и отправляющая сообщение по указанному адресу"""
    msg = pickle.dumps([cmd, param])
    client.sendto(msg, (IP, PORT))

def SetSpeed(leftSpeed, rightSpeed):
    SendCommand("speed", (leftSpeed, rightSpeed))
    
def Beep():
    SendCommand("beep")
def Exit():
    SendCommand("exit")
    
SPEED = 200
IP = "127.0.0.1" #айпи сервера
PORT = 8000 #порт сервера

running = True

screen = pygame.display.set_mode([640, 480]) #создаем окно программы
clock = pygame.time.Clock()
pygame.joystick.init()

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #создаем udp клиент

while running:
    for event in pygame.event.get(): #пробегаемся в цикле по всем событиям Pygame
        #print(event)
        if event.type == pygame.QUIT: #проверка на выход из окна
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                SetSpeed(SPEED, -SPEED)
            elif event.key == pygame.K_RIGHT:
                SetSpeed(-SPEED, SPEED)
            elif event.key == pygame.K_UP:
                SetSpeed(SPEED, SPEED)
            elif event.key == pygame.K_DOWN:
                SetSpeed(-SPEED, -SPEED)
            elif event.key == pygame.K_SPACE:
                Beep()
        elif event.type == pygame.KEYUP:
            SetSpeed(0,0)
        elif event.type == pygame.K_HOME:
            setSpeed(0, 0)
            Exit()
            running = False
            break
pygame.quit()
client.close()
