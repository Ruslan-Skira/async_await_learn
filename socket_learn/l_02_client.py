import socket
# https://www.youtube.com/watch?v=btmi2JmAwxY
socket_server = socket.socket()
name = input("Fill up your name please")
socket_server.connect(("127.0.0.1", 12345))
socket_server.send(name.encode())
socket_data = socket_server.recv(1024)
server_name = socket_data.decode()
print(server_name, "connected")

while True:
    message = socket_server.recv(1024).decode()
    print(server_name, ":", message)
    message = input("I'm: ")
    socket_server.send(message.encode())

