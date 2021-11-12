from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired


class Loginform(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    name_family = StringField(validators=[DataRequired()])
    
    def Ldata(self):
        return {
            "username":self.username,
            "password":self.password,
            "Name & Family": self.name_family
        }