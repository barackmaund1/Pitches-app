from . import db
from datetime import datetime


category_post = db.Table('category_post',
                         db.Column('posts_id', db.Integer, db.ForeignKey('posts.id')),
                         db.Column('categories_id', db.Integer, db.ForeignKey('categories.id'))
)



class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    en_name = db.Column(db.String(128))
    en_url = db.Column(db.String(128))
    de_name = db.Column(db.String(128))
    de_url = db.Column(db.String(128))

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    active = db.Column(db.Boolean, default="0")
    categories = db.relationship('Category',
                                 secondary=category_post,
                                 backref=db.backref('posts', lazy='dynamic'),
                                 lazy='dynamic')
    comments = db.relationship('Comment', backref='post', lazy='dynamic')
    en_title = db.Column(db.String(128))
    de_title = db.Column(db.String(128))
    en_subtitle = db.Column(db.String(128))
    de_subtitle = db.Column(db.String(128))
    en_description = db.Column(db.String(256))
    de_description = db.Column(db.String(256))
    en_body = db.Column(db.Text)
    de_body = db.Column(db.Text)
    en_url = db.Column(db.String(128))
    de_url = db.Column(db.String(128))


class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name}'

    
