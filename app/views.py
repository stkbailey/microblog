from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'} # fake user
	posts = [ #fake array of posts
		{'author': {'nickname': 'John'},
		 'body': 'Beautiful day in Portland!'},
		{'author': {'nickname': 'Susan'}, 
		 'body': 'The Avengers movie was so cool!'},
		{'author': {'nickname': 'Jared'}, 
		 'body': 'Wub a lub a dub dub!'}
		]
	return render_template('index.html', 
							title='Home', 
							user=user,
							posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="{}", remember_me={}'.format(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')

	return render_template('login.html', 
							title='Login',
							form=form,
							providers=app.config['OPENID_PROVIDERS'])