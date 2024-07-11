#!/usr/bin/env python3
from api.v1.views.index import *
from api.v1.views.users import *
from flask import Blueprint
""" DocDocDocDocDocDoc """

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

User.load_from_file()
