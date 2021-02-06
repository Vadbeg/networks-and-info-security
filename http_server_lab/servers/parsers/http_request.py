"""Module with HTTP request string parser"""

from typing import List, Tuple, Optional

from http_server_lab.utils.errors import BadRequestError


class HTTPRequest:

    def __init__(self, data):
        self.method: Optional[str] = None
        self.uri: Optional[str] = None

        self.http_version: str = '1.1'

        self.__parse(data)

    @staticmethod
    def __get_request_line(lines: List[bytes]) -> bytes:
        try:
            request_line = lines[0]
        except IndexError as err:
            raise BadRequestError

        return request_line

    @staticmethod
    def __parse_request_line(request_line: bytes) -> Tuple[str, str, str]:
        request_line_words = request_line.split(b' ')

        request_method = request_line_words[0].decode()

        request_uri = None
        request_http_version = None

        try:
            request_uri = request_line_words[1].decode()
            request_http_version = request_line_words[2].decode()
        except IndexError:
            pass

        return request_method, request_uri, request_http_version

    def __parse(self, data: bytes):
        lines = data.split(b'\r\n')

        request_line = self.__get_request_line(lines=lines)

        request_method, request_uri, request_http_version = self.__parse_request_line(
            request_line=request_line
        )

        self.method = request_method

        if request_uri:
            self.uri = request_uri

        if request_http_version:
            self.http_version = request_http_version

