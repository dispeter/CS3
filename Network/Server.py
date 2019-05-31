import socket

host = '192.168.102.179'
port = 42069

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET tells su we're using IP addresses with 4 bytes
#socket.SOCK_STREAM tells us that we're using TCP/IP

my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
my_socket.bind((host, port))
#secures link between host and port while program is running

maintain_connection = True

while maintain_connection:
    my_socket.listen()
    connection, address = my_socket.accept()
    while True:
        data = connection.recv(1024)
        data = data.decode('utf-8')
        if not data:
            break
        print(str(address[0]) + ': ' , data)
    connection.close()
# maintain_connection = False   
my_socket.close()


































