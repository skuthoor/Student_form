from project import db, login_manager
from project import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

class student(db.Model,UserMixin):
	id = db.Column(db.Integer(), primary_key=True)
	student_name = db.Column(db.String(length=30),nullable=False)
	college_name = db.Column(db.String(length = 30), nullable= False)
	specialistion = db.Column(db.String(length = 40),nullable= False)
	degree_name = db.Column(db.String(length = 40), nullable= False)
	internship = db.Column(db.String(length = 40),nullable= False)
	phone_no = db.Column(db.Integer(), nullable= False,unique=True)
	email_address = db.Column(db.String(length=50), nullable=False, unique=True)
	location = db.Column(db.String(length = 40),nullable= False)
	Gender = db.Column(db.String(),nullable= False)
	note = db.Column(db.String(length = 200),nullable= False)


class user(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False )
    password_hash = db.Column(db.String(length=60), nullable=False)                       
    # user_status = db.Column(db.String(length=30), nullable =True  )

    # @property
    # def password(self):
    # 	return self.password

    # @password.setter
    # def password(self,plain_text_password):
    # 	self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
	
    # def check_password_correction(self, attempted_password):
    #     return bcrypt.check_password_hash(self.password_hash, attempted_password)
