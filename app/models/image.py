from app.extensions import db

class Image(db.Model):
  __tablename__ = 'images'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  img = db.Column(db.String(128), nullable=False)
  
  gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'))

  def __repr__(self):
    return f'<Lake_pic {self.title}>'