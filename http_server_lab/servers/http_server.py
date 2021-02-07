
import os
import mimetypes
from typing import Dict, Optional

from http_server_lab.servers.tcp_server import TCPServer
from http_server_lab.servers.parsers.http_request import HTTPRequest


class HTTPServer(TCPServer):

    HEADERS = {
        'Server': 'Simple Server',
        'Content-Type': 'text/html'
    }

    STATUS_CODES = {
        200: 'OK',
        201: 'Created',
        404: 'No Found',
        501: 'Not Implemented'
    }

    def __init__(self, host='127.0.0.1', port=8888, data_folder: str = 'data'):
        super().__init__(host=host, port=port)

        self.data_folder = data_folder

    def handle_request(self, data) -> bytes:
        """
        Handles request and performs data preprocessing

        :param data: data from request
        :return: response
        """

        request = HTTPRequest(data=data)

        try:
            handler = getattr(self, f'handle_{request.method}')
        except AttributeError:
            handler = self.handle_HTTP_501

        response = handler(request)

        return response

    def handle_HTTP_501(self, request: HTTPRequest) -> bytes:
        response_line = self.response_line(status_code=501)

        response_headers = self.response_headers()

        blank_line = b'\r\n'

        response_body = b"<h1>501 Not Implemented</h1>"

        response = b''.join([
            response_line, response_headers,
            blank_line, response_body
        ])

        return response

    def handle_POST(self, request: HTTPRequest) -> bytes:
        """Handler for POST HTTP method"""

        response_line = self.response_line(status_code=200)

        blank_line = b'\r\n'

        data_repository = request.data_repository
        data_repository.save(folder=self.data_folder)

        response = b''.join([
            response_line, blank_line
        ])

        return response

    def handle_OPTIONS(self, request: HTTPRequest) -> bytes:
        """Handler for OPTIONS HTTP method"""

        filename = request.uri.strip('/')

        response_line = self.response_line(200)

        extra_headers = {'Allow': 'OPTIONS, GET, POST'}

        if os.path.exists(filename) and not os.path.isdir(filename):
            content_type = mimetypes.guess_type(url=filename)[0] or 'text/html'
            extra_headers.update(
                {'Content-Type': content_type}
            )

        response_headers = self.response_headers(extra_headers=extra_headers)
        blank_line = b'\r\n'

        response = b''.join([
            response_line, response_headers, blank_line
        ])

        return response

    def handle_GET(self, request: HTTPRequest) -> bytes:
        """Handler for GET HTTP method"""

        filename = request.uri.strip('/')

        blank_line = b'\r\n'

        if os.path.exists(filename) and not os.path.isdir(filename):
            response_line = self.response_line(status_code=200)

            content_type = mimetypes.guess_type(url=filename)[0] or 'text/html'
            extra_headers = {'Content-Type': content_type}

            response_headers = self.response_headers(extra_headers=extra_headers)

            with open(file=filename, mode='rb') as file:
                response_body = file.read()
        else:
            response_line = self.response_line(status_code=404)
            response_headers = self.response_headers()
            response_body = b"<h1>404 Not Found</h1>"

        response = b''.join([
            response_line, response_headers,
            blank_line, response_body
        ])

        return response

    def response_line(self, status_code: int) -> bytes:
        """
        Creates status line from status_code

        :param status_code: raw status code
        :return: prepared status line
        """

        reason = self.STATUS_CODES[status_code]

        line = f'HTTP/1.1 {status_code} {reason}\r\n'

        return line.encode()

    def response_headers(self, extra_headers: Optional[Dict] = None) -> bytes:
        """
        Creates response headers

        :param extra_headers: additional headers for response
        :return: headers converted to bytes string
        """

        headers_copy = self.HEADERS.copy()

        if extra_headers:
            headers_copy.update(extra_headers)

        headers = ''

        for header_type, header_text in headers_copy.items():
            headers += f'{header_type}: {header_text}\r\n'

        return headers.encode()
