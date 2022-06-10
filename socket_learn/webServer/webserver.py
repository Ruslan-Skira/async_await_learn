import socket

server = socket.socket()
server.bind(("127.0.0.1", 8000))
server.listen()
print("server started")
while True:
    client_socket, add = server.accept()
    data = client_socket.recv(1024).decode("utf-8")
    print(data)
    HDRS= "HTTP/1.1 200 OK\r\nContent-Type:text/html; charset=utf-8\r\n\r\n".encode("utf-8")
    content = "HI user".encode("utf-8")
    client_socket.send(HDRS+content)
    client_socket.shutdown(socket.SHUT_WR)