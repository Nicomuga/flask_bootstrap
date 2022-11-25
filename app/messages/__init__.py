from flaskk import Blueprint

bp = blueprint('messages', __name__)

from app.messages import routes