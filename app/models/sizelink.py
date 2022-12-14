from app.extensions import db


class Sizelink(db.Model):
  __tablename__ = 'sizes'
  id = db.Column(db.Integer, primary_key=True)
  link = db.Column(db.String(128), nullable=False)
  size = db.Column(db.String(120), nullable=False)
  price = db.Column(db.Integer)

  def __repr__(self):
    return f'<Sizelink {self.title}>'
