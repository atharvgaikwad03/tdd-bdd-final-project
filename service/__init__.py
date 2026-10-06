"""
Service Package
"""
from flask import Flask

app = Flask(__name__)

from service import routes, models  # noqa: F401, E402
