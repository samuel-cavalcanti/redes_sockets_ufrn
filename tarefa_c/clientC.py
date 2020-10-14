from socket import *
import sys


def connect_server():
    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    while True:
        completed_command = clientSocket.recv(1024).decode()

        print('From Server: ', completed_command)

        message: str = input('>>')
        # display_message(message)
        clientSocket.send(message.encode())

    clientSocket.close()


connect_server()