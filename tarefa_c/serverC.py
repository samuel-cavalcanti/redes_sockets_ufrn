from socket import *
import subprocess


def start_server():
    server_port = 12000
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    tcp_server_socket.bind(('', server_port))
    number_of_max_connections = 1
    tcp_server_socket.listen(number_of_max_connections)

    print('The server is ready to receive')

    while True:
        connected_socket, addr = tcp_server_socket.accept()
        connected_socket.send('connection sucess'.encode())

        while socket_connection_is_alive(connected_socket):
            pass

    pass


def socket_connection_is_alive(tcp_client: socket) -> bool:
    amount_of_data_to_be_received_at_once_in_bytes = 1024
    client_command = tcp_client.recv(
        amount_of_data_to_be_received_at_once_in_bytes).decode()

    if have_no_command(client_command):
        output_message = "error: must type any command"
    else:
        output_message = run_command_in_sub_process(client_command)

    sucess = try_send_message_to_tcp_client(output_message, tcp_client)

    if not sucess:
        print('Unable to send message to client, closing connection')
        tcp_client.close()

    return sucess


def have_no_command(message: str) -> bool:
    return len(message) == 0


def run_command_in_sub_process(socket_message: str) -> str:

    try:
        command_and_args = socket_message.split(' ')

        completed_sub_process = subprocess.run(
            command_and_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        return f"{completed_sub_process.stdout.decode()} \n {completed_sub_process.stderr.decode()}"
    except Exception as command_error:
        return f"Exception: {command_error}!"


def try_send_message_to_tcp_client(message: str, tcp_client: socket) -> bool:
    try:
        tcp_client.send(message.encode())
        return True

    except Exception as connection_error:
        return False


start_server()