from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required


class LoginForm(Form):
   
    name = StringField('НЭР', validators=[Required()])
    room = StringField('ОРОН ЗАЙ', validators=[Required()])
    submit = SubmitField('ЧАТД НЭГДЭХ')
