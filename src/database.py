
from datetime import datetime
import string as String 
import random
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50), unique=True, nullable=False)
    email=db.Column(db.String(50), unique=True, nullable=False)
    password=db.Column(db.String(50), nullable=False)
    created_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    Bookmarks=db.relationship('Bookmark', backref='user', lazy=True)
    

    def __repr__(self):
        return 'User>>> {self.username}'


    

class Bookmark(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    body=db.Column(db.Text, nullable=False)
    url=db.Column(db.Text, nullable=False)
    short_url=db.Column(db.String(3), nullable=False)
    visits=db.Column(db.Integer, nullable=False, default=0)
    created_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    
    
    def generate_short_characters(self):
        characters=String.digits+String.ascii_letters
        picked_chars=''.join(random.choices(characters, k=3))
        links=self.query.filter_by(short_url=picked_chars).first()
        if links :
            self.generate_short_characters()
        else:
            return picked_chars
        
    def __init__(self,**kwargs,) :
        super().__init__(**kwargs)
        self.short_url=self.generate_short_characters()
  
    def __repr__(self):
        return 'Bookmark>>> {self.url}'
    
    

    
 
    

        
        
