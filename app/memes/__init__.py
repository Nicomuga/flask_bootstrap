from flask import Blueprint

bp = Blueprint('memes', __name__)

from app.main import routes