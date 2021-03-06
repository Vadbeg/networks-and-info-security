"""Server starting script"""

import sys
sys.path.append('/home/vadbeg/Projects/University/networks-and-info-security')

import argparse
from modules.api import create_app


def get_args():
    parser = argparse.ArgumentParser(description=f'Script for business documentation app starting.')

    parser.add_argument('--app-host', type=str, default='0.0.0.0', help='Host for the app')
    parser.add_argument('--app-port', type=int, default=9000, help='Port for the app')

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = get_args()

    app_host = args.app_host
    app_port = args.app_port

    app = create_app()
    app.run(host=app_host, port=app_port)

