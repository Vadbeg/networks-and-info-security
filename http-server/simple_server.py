import socket


def create_socket(host: str = '', port: int = 8888):
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((host, port))

    listen_socket.listen(1)

    return listen_socket


def accept_request(listen_socket: socket.socket):
    client_connection, client_address = listen_socket.accept()

    request_data = client_connection.recv(1024)

    print(request_data.decode('UTF-8'))

    http_response = b"""
HTTP/1.1 200 OK

Hello, World!     
    """

    client_connection.sendall(http_response)
    client_connection.close()


if __name__ == '__main__':
    HOST = ''
    PORT = 8888

    listen_socket = create_socket(host=HOST, port=PORT)

    print(f'Serving HTTP on port {PORT}.')

    while True:
        accept_request(listen_socket=listen_socket)


