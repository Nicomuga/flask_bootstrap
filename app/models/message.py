from app.extensions import db


class Message(db.Model):
  __tablename__ = 'messages'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128), nullable=False)
  content = db.Column(db.Text, nullable=False)
  picture = db.Column(db.String(300))
  type_of = db.Column(db.String(20), nullable=False)
  price = db.Column(db.Integer)
 


  #Stablish the relation between table messages and users, between model user and model message
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def __repr__(self):
    return f'<Message {self.title}>'
