"""Module with utilities for user authentication"""

import os
import requests
from typing import Tuple, Dict


def get_google_provider_cfg() -> Dict:
    google_discovery_url = os.environ.get('GOOGLE_DISCOVERY_URL', None)

    response = requests.get(google_discovery_url)
    response = response.json()

    return response


def parse_user_info(user_info: Dict) -> Tuple:
    user_email = user_info.get('email')

    return user_email
