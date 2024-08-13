import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))
server.listen(1)

conn, addr = server.accept()
with open('/root/flag.txt', 'r') as file:
    conn.sendall(file.read().encode())
conn.close()
