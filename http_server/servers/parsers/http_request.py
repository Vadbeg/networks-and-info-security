"""Module with HTTP request string parser"""

from typing import Dict, List, Tuple, Optional

from http_server.utils.errors import BadRequestError
from http_server.servers.parsers.data_parser import DataParser


class HTTPRequest:

    def __init__(self, data):
        self.method: Optional[str] = None
        self.uri: Optional[str] = None

        self.http_version: str = '1.1'

        self.data_repository: Optional[DataParser] = None

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

        if request_method == 'POST':
            self.data_repository = DataParser(raw_data=data)


