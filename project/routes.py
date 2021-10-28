#! /usr/bin/python3
from project import app
from flask import render_template,redirect,url_for,flash, request
from project.models import user, student
from project.forms import userform, studentform
from project import db
from flask_login import login_user, logout_user,login_required, current_user


@app.route('/')
def home():
	return render_template('home.html')
@app.route('/select')
def select_page():
	return render_template('select.html')

@app.route('/user', methods=['GET','POST'])
def register_page():
	form = studentform()
	# form2 = userform()
	if form.validate_on_submit():
		user_to_create = student(student_name=form.student_name.data,college_name=form.college_name.data,specialistion=form.specialistion.data,degree_name=form.degree_name.data,internship=form.internship.data,phone_no=form.phone_no.data,email_address=form.email_address.data,location=form.location.data,Gender = form.Gender.data, note = form.note.data)
		
		db.session.add(user_to_create)
		db.session.commit()

		user1_to_create = user(username = form.email_address.data,password_hash= form.phone_no.data)
		db.session.add(user1_to_create)
		db.session.commit()
		
		login_user(user_to_create)
		flash(f'user is succesfully registered',category='success')
		return redirect(url_for('register_page'))
		# return redirect(url_for('home'))
	if form.errors != {}: #if  errors in validatn
		for err_msg in form.errors.values():
			flash(f'There was an error in creating a user:{err_msg}', category='danger')
	
	


		return redirect(url_for('register_page'))
		
	
	return render_template('register.html',form=form)
	# return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login_page():
	form2 = userform()

	if form2.validate_on_submit():
				
		attempted_user = user.query.filter_by(username=form2.username.data).first()
		attempted_pass = user.query.filter_by(password_hash= form2.password1.data)
		if attempted_user and attempted_pass:
			login_user(attempted_user)
			flash(f'Sucess! You are logged in as: {attempted_user.username}',category = 'success')
			return redirect(url_for('user_page'))
		else:
			flash('Username or Password is incorrect! Please try again', category= 'danger')


		return redirect(url_for('register_page'))
		
	if form2.errors != {}: #if  errors in validatn
		for err_msg in form2.errors.values():
			flash(f'There was an error in creating a user:{err_msg}', category='danger')
	return render_template('login.html',form = form2)


@app.route('/logout')
def logout_page():
	logout_user()
	flash('You have been logged out!',category='info')
	return redirect(url_for('home'))

@app.route('/user/login',methods =['GET'])
def user_page():
	y = student.query.filter_by(email_address=current_user.username).first()
	return render_template('user.html',y=y)
