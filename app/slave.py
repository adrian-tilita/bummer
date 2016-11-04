import socket

socketConnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketConnection.connect(('127.0.0.1', 5001))

for i in range(0, 2):
    socketConnection.send("A message")
