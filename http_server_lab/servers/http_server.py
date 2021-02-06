
from typing import Dict, Optional

from http_server_lab.servers.tcp_server import TCPServer


class HTTPServer(TCPServer):

    HEADERS = {
        'Server': 'Simple Server',
        'Content-Type': 'text/html'
    }

    STATUS_CODES = {
        200: 'OK',
        404: 'No Found'
    }

    def handle_request(self, data) -> bytes:
        """
        Handles request and performs data preprocessing

        :param data: data from request
        :return: response
        """
        print(f'Data: {data}')

        response_line = self.response_line(status_code=200)
        response_headers = self.response_headers(extra_headers=None)

        blank_line = b'\r\n'

        response_body = b'''
<html>
    <body>
        <h1>Request received!</h1>
    </body>
</html>
        '''

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
