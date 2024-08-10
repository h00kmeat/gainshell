import socket

def start_listener(host='0.0.0.0', port=4444):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f'Listening on {host}:{port}...')
        conn, addr = s.accept()
        with conn:
            print(f'Connection from {addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

start_listener()
