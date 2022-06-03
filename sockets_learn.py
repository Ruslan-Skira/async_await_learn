import socket

# Server part
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5001))
server_socket.listen()

# Client
while True:
    print('Before .accept()')

    client_socket, addr = server_socket.accept()  # blocking our socket

    print('Connection from', addr)

    while True:
        print('Before .recv()')
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = "hello python dev \n".encode()
            client_socket.send(response)
