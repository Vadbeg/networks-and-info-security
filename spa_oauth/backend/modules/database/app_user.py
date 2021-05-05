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

        # password = bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())
        password = hash(password.encode())

        print(f'Generated: {password}')

        add_app_user_query = """
        INSERT INTO app_user (email, password)
        VALUES (%s, %s)
        RETURNING id;
                """

        print(password)

        val = [email, password]

        self.cursor.execute(add_app_user_query, val)
        self.connection.commit()

        new_user_id = self.cursor.fetchone()[0]

        return new_user_id

    @staticmethod
    def check_correct_password(input_password: str, old_password_hash: str) -> bool:
        input_password_hash = hash(input_password.encode())

        is_correct_password = input_password_hash == old_password_hash

        print(f'Input', input_password_hash)
        print(f'Output', old_password_hash)
        print(f'is_correct_password', is_correct_password)

        return is_correct_password

    def get_app_user_by_email(
            self, email: str,
    ) -> Dict[str, str]:
        """
        Adds new user to database

        :param email: user email
        :return: id of the new user
        """

        add_app_user_query = """
        SELECT *
        FROM app_user
        WHERE email=%s;
                """

        val = [email]

        self.cursor.execute(add_app_user_query, val)
        self.connection.commit()

        all_users_with_given_email = self.cursor.fetchall()

        if (all_users_with_given_email is None) or (len(all_users_with_given_email) == 0):
            user_with_given_id = None
        else:
            user_with_given_id = all_users_with_given_email[0]
            user_with_given_id = dict(zip(self.COLUMNS, user_with_given_id))

        print(user_with_given_id)

        return user_with_given_id

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
