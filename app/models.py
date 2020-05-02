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
    upvote = db.relationship('Upvote',backref='pitch',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='pitch',lazy='dynamic')
    en_title = db.Column(db.String(128))
    en_subtitle = db.Column(db.String(128))
    en_description = db.Column(db.String(256))
    en_body = db.Column(db.Text)
    en_url = db.Column(db.String(128))

    def save_post(self):
        db.session.add(self)
        db.session.commit()

        
    def __repr__(self):
        return f'Post {self.post}'
    


class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    posts=db.relationship('Post',backref='user',lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvote = db.relationship('Upvote',backref='pitch',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='pitch',lazy='dynamic')


    def __repr__(self):
        return f'User {self.username}'

    
class Comment(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer,primary_key = True)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_comment=db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    
   
    

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_comments(cls,id):
        comments=Comment.query.filter_by(post_id=id).all()
        return comments

    def __repr__(self):
        return f'comment:{self.comment}'    


class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls,id):
        upvote = Upvote.query.filter_by(post_id=id).all()
        return upvote


    def __repr__(self):
        return f'{self.user_id}:{self.post_id}' 

class Downvote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    

    def save(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_downvotes(cls,id):
        downvote = Downvote.query.filter_by(post_id=id).all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.post_id}'               
            