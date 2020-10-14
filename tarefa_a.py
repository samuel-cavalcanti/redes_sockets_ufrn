import socket as socket_module

from arg_parse_socket_homework import ArgParseSocketHomework
from tarefa_a.time_server import TimeServer

server_port = 6000
server_address = 'localhost'


def start_udp_server():
    server_udp = socket_module.socket(socket_module.AF_INET, socket_module.SOCK_DGRAM)
    server_udp.bind((server_address, server_port))
    waiting_for_connections(server_udp)


def waiting_for_connections(server_udp: socket_module.socket):
    time_server = TimeServer()
    print(f'start time server to connections {server_address} port: {server_port}')
    while True:
        message, client_address = server_udp.recvfrom(2048)
        output_message = time_server.response(message)
        server_udp.sendto(output_message, client_address)


def start_udp_client():
    client_udp = socket_module.socket(socket_module.AF_INET, socket_module.SOCK_DGRAM)
    client_udp.bind(('', 61000))
    send_message_to_server(client_udp, server_address, server_port)


def send_message_to_server(client_udp: socket_module.socket, address: str, port: int):
    buffer_size = 1024
    while True:
        command = input('>>')
        client_udp.sendto(command.encode(), (address, port))
        time_in_bytes, _ = client_udp.recvfrom(buffer_size)
        print(time_in_bytes.decode())


tarefa_a = ArgParseSocketHomework(start_client_callback=start_udp_client, start_server_callback=start_udp_server,
                                  description='Desenvolver um servidor de data')

tarefa_a.parse()
