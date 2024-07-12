#!/usr/bin/env python3
""" Session Expiry Auth class module """
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """ Session Expiry Auth class """
    def __init__(self):
        """ Constructor """
        try:
            session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            session_duration = 0
        self.session_duration = session_duration

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for a user_id """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns a User ID based on a Session ID """
        if session_id is None or not isinstance(session_id, str):
            return None

        user_dict = SessionAuth.user_id_by_session_id.get(session_id)
        if user_dict is None:
            return None

        user_id = user_dict.get('user_id')
        created_at = user_dict.get('created_at')

        if self.session_duration <= 0:
            return user_id

        if created_at is None:
            return None

        offsetTime = timedelta(seconds=self.session_duration)
        if (created_at + offsetTime) < datetime.now():
            return None

        return user_id
