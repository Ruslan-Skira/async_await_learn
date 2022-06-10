import socket
new_socket = socket.socket()
new_socket.bind(("127.0.0.1", 12345))  # open for other processes
new_socket.listen()

print('I"m running')
user_name = input('Fill up your name')
conn, add = new_socket.accept()  # register all  clients which are connected to us
client = (conn.recv(1024).decode())
print(f"{client} Connected")
conn.send(user_name.encode())
while True:
    message = input("I'm: ")
    conn.send(message.encode())
    message_client = conn.recv(1024)
    message_client = message_client.decode()
    print(f"{client}, : {message_client}")

