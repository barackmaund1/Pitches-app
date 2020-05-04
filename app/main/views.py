from flask import render_template,request,redirect,url_for,abort,app,flash
from . import main
from ..models import Post,User,Comment,Upvote,Downvote
from flask_login import login_required,login_user, current_user, logout_user
from .. import  db,photos
import os
import secrets
from .. import db,photos
from .forms import UpdateAccountForm,NewPost
from PIL import Image

@main.route('/')
def index():
    general=Post.query.all()
    bible=Post.query.filter_by(category='bible').all()
    motivation=Post.query.filter_by(category='bible').all()
    love=Post.query.filter_by(category='bible').all()
    return render_template('index.html',general=general,bible=bible,motivation=motivation,love=love)

@main.route('/new_post',methods = ['POST','GET'])
@login_required
def new_post():
    form=NewPost()
    if form.validate_on_submit():
        user_id=current_user
        new_post=Post(title=form.title.data,author=form.author.data,description=form.description.data,category=form.category.data,
        user_id =current_user._get_current_object())
        new_post.save_post()
        # db.session.add(new_post)
        # db.session.commit()
        flash('Your pitch has been created!','success')
        return redirect(url_for('main.index'))
    return render_template('new_post.html',title='New pitch',form=form,legend='New Post')  
@main.route('/comment/<int:post_id>', methods = ['POST','GET'])
@login_required
def comment(post_id):
    form = CommentForm()
    post = Post.query.get(post_id)
    all_comments = Comment.get_comments
    if form.validate_on_submit():
        comment = form.comment.data 
        post_id = post_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,post_id = post_id)
        new_comment.save_comment()
        return redirect(url_for('main.comment', pitch_id = pitch_id))
    return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)      

@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def upvote(id):
    get_posts = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for post in get_posts:
        to_str = f'{post}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, post_id=id)
    new_vote.save()
    return redirect(url_for('main.index',id=id))

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def downvote(id):
    posts = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for post in posts:
        to_str = f'{post}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, post_id=id)
    new_downvote.save()
    return redirect(url_for('main.index',id = id))
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(main.root_path, 'static/photos', picture_fn)
    form_picture.save(picture_path)
     
    output_size=(125,125)
    i=Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

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



