from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField,TextAreaField,SelectField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError,Required
from ..models import User


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose another')

class NewPost(FlaskForm):
    title= StringField('Title', validators=[Required()])  
    author=StringField('Author', validators=[Required()]) 
    description=TextAreaField('Your Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('Bible','Bible'),('Motivation','Motivation'),('Love','Love')],validators=[Required()])
    submit = SubmitField('Pitch')
class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')  