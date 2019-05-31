import socket

host = "192.168.100.87" #special ip address called a loop back
port = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
    my_socket.connect((host, port))
    while True:
        my_socket.sendall(b"Sub to pewdiepie")
        my_socket.sendall(b"ddos")

    



















