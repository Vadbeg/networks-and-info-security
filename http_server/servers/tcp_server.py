"""Module with TCP server implementation"""

import time
import socket


class TCPServer:
    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host
        self.port = port

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.host, self.port))
        s.listen(5)

        print("Listening at", s.getsockname())

        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            data = conn.recv(1024 * 100_000)
            conn.settimeout(0.5)

            counter = 0
            while True:

                try:
                    new_data = conn.recv(1024)
                    data += new_data
                except socket.timeout as err:
                    print(f'Socket timed out!')
                    break

                counter += 1

                if new_data == b'':
                    print(f'Received additional {counter * 20} bytes of data')
                    break

            response = self.handle_request(data)

            res = conn.sendall(response)
            conn.shutdown(socket.SHUT_WR)

            counter = 0
            while True:
                new_data = conn.recv(20)
                counter += 1

                if new_data == b'':
                    print(f'Received garbage {counter * 20} bytes of data')
                    break

            conn.close()

    def handle_request(self, data):
        """Handles incoming data and returns a response.
        Override this in subclass.
        """
        return data


