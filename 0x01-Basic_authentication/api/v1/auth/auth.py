#!/usr/bin/env python3
""" Auth class module """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for validating if endpoint requires auth """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        
        if path[-1] != '/':
            path += '/'
        
        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user """
        return None
