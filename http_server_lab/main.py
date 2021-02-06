"""Server starting script"""


from http_server_lab.servers.http_server import HTTPServer


if __name__ == '__main__':
    server = HTTPServer()
    server.start()
