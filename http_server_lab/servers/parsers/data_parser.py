"""Module with POST data parser"""

import os
from typing import Optional, List


class DataParser:

    def __init__(self, raw_data: bytes):
        self.__raw_data = raw_data

        self.filename: Optional[str] = None
        self.content_type: Optional[str] = None
        self.data: Optional[bytes] = None

        self.__parse()

    def __parse(self):
        lines = self.__raw_data.split(b'\r\n')

        data_start_index = self.__get_start_data_index(lines=lines)
        lines = lines[data_start_index:]

        self.filename = self.__get_filename(lines=lines)
        self.content_type = self.__get_content_type(lines=lines)

        self.data = self.__get_data(lines=lines)

    def save(self, folder: str):
        data_path = os.path.join(folder, self.filename)

        with open(file=data_path, mode='wb') as file:
            file.write(self.data)

    @staticmethod
    def __get_filename(lines: List[bytes]) -> str:
        raw_data_info = lines[0].split(b';')
        raw_data_info = [curr_data_info.strip() for curr_data_info in raw_data_info]

        filename = raw_data_info[-1].split(b'=')[-1].strip().decode()

        filename = filename.replace('\"', '')

        return filename

    @staticmethod
    def __get_content_type(lines: List[bytes]) -> str:
        content_type = lines[1].split(b':')[-1].strip().decode()

        return content_type

    @staticmethod
    def __get_data(lines: List[bytes]) -> bytes:
        data = b'\r\n'.join(lines[3:-2])

        return data

    @staticmethod
    def __get_start_data_index(lines: List[bytes]) -> int:
        data_start_index = -1

        for idx, curr_line in enumerate(lines):
            if b'Content-Disposition' in curr_line:
                data_start_index = idx

        if data_start_index == -1:
            raise IndexError(f'No data in request!')

        return data_start_index
