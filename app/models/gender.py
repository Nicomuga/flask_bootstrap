from app.extensions import db

class Gender(db.Model):
  __tablename__ = 'genders'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  description = db.Column(db.Text, nullable=False)
  
  images = db.relationship('Image', backref = 'gender')  

  def __repr__(self):
    return f'<Lake {self.title}>'