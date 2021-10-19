# msgtest.py
#
# Un programa que envía un mensaje al servidor de muestra en genmessages.py

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
def send_msg(msg):
    s.sendto(msg, ("",10000))

send_msg(b"Hola soy un cliente")