import socket

socketConnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketConnection.bind(('127.0.0.1', 5001))

waitForSingnals = True
waitForMessage = False

while waitForSingnals:
    data, addr = socketConnection.recvfrom(1024)  # buffer size is 1024 bytes
    print("received message:" + str(data))