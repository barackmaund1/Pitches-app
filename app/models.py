from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic')
    upvote = db.relationship('Upvote',backref='post',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='post',lazy='dynamic')
    title = db.Column(db.String(255),nullable = False)
    author= db.Column(db.String(255),nullable = False)
    description = db.Column(db.Text(),nullable = False)
    category=db.Column(db.String(255),index=True,nullable=False)

    def save_post(self):
        db.session.add(self)
        db.session.commit()
    
    
    def __repr__(self):
        return f'Post {self.title},{self.author},{self.description},{self.category}'
    
class User(db.Model,UserMixin):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique=True,nullable=False)
    posts=db.relationship('Post',backref='user',lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvote = db.relationship('Upvote',backref='user',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='user',lazy='dynamic')
    email = db.Column(db.String(120),unique=True,nullable=False)
    pass_secure=db.Column(db.String(120),nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    bio = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User"{self.username}","{self.email}","{self.image_file}"'

    
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
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    
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
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_downvotes(cls,id):
        downvote = Downvote.query.filter_by(post_id=id).all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.post_id}'               
            