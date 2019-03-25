from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, Length, DataRequired

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email(), Length(0,64)])
    password = StringField('Senha', validators=[DataRequired()])
    submit = StringField('Logar')

class RegisterForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired(), Length(0,50)])
    email = StringField('E-mail', validators=[DataRequired(), Email(), Length(0,64)])
    password = StringField('Senha', validators=[DataRequired()])
    submit = StringField('Logar')

class TodoForm(FlaskForm):
        title = StringField('Título', validators=[DataRequired, Length(0,40)])


