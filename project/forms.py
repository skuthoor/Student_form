from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from project.models import user

class studentform(FlaskForm):

	student_name = StringField(label = 'Student Name',validators=[Length(min=2,max=30),DataRequired()])
	college_name = StringField(label = 'College Name',validators=[Length(min=2,max=30),DataRequired()])
	specialistion = StringField(label = 'Specialistion',validators=[Length(min=2,max=30),DataRequired()])
	degree_name = StringField(label = 'Degree Name',validators=[Length(min=2,max=30),DataRequired()])
	internship = StringField(label = 'Internship Applied for',validators=[Length(min=2,max=30),DataRequired()])
	phone_no =  StringField(label='Phone Number', validators=[Length(min=4),DataRequired()])
	email_address = StringField(label="Email Address", validators=[Email(),DataRequired()])
	location = StringField(label = 'Location',validators=[Length(min=2,max=30),DataRequired()])
	Gender = SelectField(label='Blood Group',choices=['Male','Female','Not Prefered to say'])
	note = StringField(label = 'Note',validators=[Length(min=2,max=100),DataRequired()])
	submit = SubmitField('Add Details')


class userform(FlaskForm):
	username = StringField(label='Name', validators=[Length(min=2,max=30),DataRequired()])
	password1 = PasswordField(label='Password', validators=[Length(min=5), DataRequired()])
	# user_staus = StringField(label='User Staus',validators= [Length(min=1,max= 30)])
	submit = SubmitField(label='Log In')



	 




