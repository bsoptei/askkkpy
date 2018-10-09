import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 7474
BUFFER_SIZE = 1024

while True:

    message = input('askkkpy:')

    if message == 'exit':
        break
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(bytes(message, 'utf-8'))
    response = s.recv(BUFFER_SIZE)
    s.close()

    print(response)
