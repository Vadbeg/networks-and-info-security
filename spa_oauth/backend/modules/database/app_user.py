"""Module with app users table interection"""

import datetime
import os
from typing import Union, List, Dict

import jwt
import bcrypt


class AppUser:
    COLUMNS = [
        'id', 'email', 'password',
    ]

    def __init__(self, connection, cursor):
        """
        Class for faster interactions with user table

        :param connection: connection to database
        :param cursor: cursor for database
        """

        self.connection = connection
        self.cursor = cursor

    def add_app_user(
            self, email: str,
            password: str
    ) -> int:
        """
        Adds new user to database

        :param email: user email
        :param password: user password
        :return: id of the new user
        """

        password = bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())
        password = 'password'

        add_app_user_query = """
        INSERT INTO app_user (email, password)
        VALUES (%s, %s)
        RETURNING id;
                """

        val = [email, password]

        self.cursor.execute(add_app_user_query, val)
        self.connection.commit()

        new_user_id = self.cursor.fetchone()[0]

        return new_user_id

    @staticmethod
    def encode_auth_token(user_id) -> Union[bytes, Exception]:
        """
        Generates  the auth token

        :param user_id: id of the user
        :return: jwt token
        """

        try:
            payload = {
                'iat': datetime.datetime.utcnow(),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'sub': user_id
            }

            token = jwt.encode(
                payload=payload,
                key=os.environ['SECRET_KEY'],
                algorithm='HS256'
            )
            print(token)

        except Exception as ex:
            raise

        return token

    @staticmethod
    def decode_auth_token(auth_token) -> Union[int, str]:
        """
        Decodes jwt auth token

        :param auth_token: jwt token
        :return: user id
        """

        payload = jwt.decode(
            jwt=auth_token,
            key=os.environ['SECRET_KEY'],
        )

        user_id = payload['sub']

        return user_id
