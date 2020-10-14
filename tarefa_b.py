import socket as socket_module

from arg_parse_socket_homework import ArgParseSocketHomework
from tarefa_b.file_server import FileServer

server_port = 6000
server_address = 'localhost'


def start_tcp_server():
    total_connections = 1
    tcp_socket = socket_module.socket(socket_module.AF_INET, socket_module.SOCK_STREAM)
    tcp_socket.bind((server_address, server_port))
    tcp_socket.listen(total_connections)

    print(f'start time server to connections {server_address} port: {server_port}')

    while True:
        client_tcp, address = tcp_socket.accept()
        while connection_is_alive(client_tcp):
            pass
        client_tcp.close()


def connection_is_alive(client_tcp: socket_module.socket) -> bool:
    file_server = FileServer()
    try:
        message_in_bytes = client_tcp.recv(1024)
        content = file_server.execute_command(message_in_bytes)
        client_tcp.send(content.encode())
        return True

    except Exception as error_socket_connection:
        print(f'connection fail {error_socket_connection}')
        return False


def start_tcp_client():
    tcp_socket = socket_module.socket(socket_module.AF_INET, socket_module.SOCK_STREAM)
    tcp_socket.connect((server_address, server_port))

    send_message_to_server(tcp_socket, server_address, server_port)


def send_message_to_server(client: socket_module.socket, address: str, port: int):
    buffer_size = 1024
    while True:
        command = input('>>')
        client.sendto(command.encode(), (address, port))
        time_in_bytes, _ = client.recvfrom(buffer_size)
        print(time_in_bytes.decode())


tarefa_b = ArgParseSocketHomework(start_server_callback=start_tcp_server, start_client_callback=start_tcp_client,
                                  description='Desenvolver um sevidor de arquivos')
tarefa_b.parse()
