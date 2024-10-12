from flask_wtf import FlaskForm 
from wtforms.fields import StringField, PasswordField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min=6) ])
    password = PasswordField('Password', [DataRequired(), Length(min=6) ])
    confirm_password = PasswordField('Confirm Password', [DataRequired(), EqualTo('password') ])
    register = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired() ])
    password = PasswordField('Password', [DataRequired()])
    login = SubmitField('Login')

class InputForm(FlaskForm):
    mean_radius =  FloatField('Mean Radius', [DataRequired() ] ,default= 17.99 ) 
    mean_perimeter = FloatField('Mean Perimeter' , [DataRequired() ], default = 122.80)
    mean_area = FloatField('mean area' , [DataRequired() ], default = 1001.0 )
    mean_concavity = FloatField('mean_concavity',[DataRequired() ], default = 30.0 )
    mean_concave_points = FloatField('mean concave points',[DataRequired() ], default = 14.0 )
    worst_radius = FloatField('worst radius',[DataRequired() ], default = 16.0 )
    worst_perimeter = FloatField('worst perimeter',[DataRequired() ], default =164.80 )
    worst_area = FloatField('worst area',[DataRequired() ], default =2019.0 )
    worst_concavity = FloatField('worst concavity  ',[DataRequired() ], default = 70.0 )
    worst_concave_points = FloatField('worst concave points',[DataRequired() ], default = 26.0 )
    send = SubmitField('Send')