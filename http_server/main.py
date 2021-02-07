"""Server starting script"""

import sys
sys.path.append('/home/vadbeg/Projects/University/networks-and-info-security')

import argparse

from http_server.servers.http_server import HTTPServer


def get_args():
    argument_parser = argparse.ArgumentParser(description=f'Script for server setup')

    argument_parser.add_argument('--port', help='Server port', type=int, default=8888)
    argument_parser.add_argument('--host', help='Server host', type=str, default='localhost')
    argument_parser.add_argument('-df', '--data-folder', help='Folder with all data', type=str, default='data')

    args = argument_parser.parse_args()

    return args


if __name__ == '__main__':
    args = get_args()

    server = HTTPServer(port=args.port, host=args.host, data_folder=args.data_folder)

    server.start()
