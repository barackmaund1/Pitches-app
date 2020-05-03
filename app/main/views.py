from flask import render_template,request,redirect,url_for,abort,app,flash
from . import main
from ..models import Category,Post,User,Comment,Upvote,Downvote
from flask_login import login_required,login_user, current_user, logout_user
from .. import  db,photos
import os
import secrets
from .. import db,photos
from .forms import UpdateAccountForm,NewPost


@main.route('/',methods = ['GET','POST'])
def index():

    bible=get_posts('bible')
    motivation=get_posts('motivation')
    love=get_posts('love')
    return render_template('index.html',bible=bible,motivation=motivation,love=love)

@main.route('/new_post',methods = ['GET','POST'])
@login_required
def new_post():
    form=NewPost()
    if form.validate_on_submit():
        title=form.title.data
        description=form.description.data
        author=form.author.data
        post=Post(title=title,description=description,author=author,user =current_user)
        post.save_post()
        flash('Your pitch has been created!','success')
        return redirect(url_for('index'))
    return render_template('new_post.html',title='New pitch',form=form,legend='New Post')    

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(main.root_path, 'static/photos', picture_fn)
    form_picture.save(picture_path)


    return picture_fn


@main.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.bio=form.bio.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('main.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='photos/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)



