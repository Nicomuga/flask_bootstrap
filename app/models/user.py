from app.extensions import db


class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(64), unique = True, index = True, nullable=False)
  username = db.Column(db.String(64), unique = True, index = True, nullable=False)
  password_hash = db.Column(db.String(128), nullable=False)

  def __repr__(self):
    return f'<Message {self.title}>'
