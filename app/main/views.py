from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Category,Post,User

@main.route('/')
def index():
    posts = Post.query.filter_by(active="1").order_by(Post.timestamp.desc())
    return render_template('index.html', posts=posts)