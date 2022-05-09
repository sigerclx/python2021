from flask import render_template
from datetime import datetime
from app import app,baseDict
from app.forms import LoginForm
from flask_login import login_required
<<<<<<< HEAD
from app.models import User,Reimbursement,Post
=======
from app.models import User,Reimbursement

@app.route('/')
@app.route('/index')
@login_required
def index():
    reimbursements = Reimbursement.query.order_by(Reimbursement.timestamp.desc()).all()
    return render_template("index.html", title='Home Page', baseDict=baseDict,reimbursements=reimbursements)

>>>>>>> parent of de53fed6 (flask报销系统的分页及bootstrap)
from flask import render_template, flash, redirect,url_for
from app import db
<<<<<<< HEAD
<<<<<<< HEAD
from flask_login import current_user, login_user
=======
=======
>>>>>>> parent of de53fed6 (flask报销系统的分页及bootstrap)
from app.forms import RegistrationForm,EditProfileForm

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)



@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        #current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',form=form)

>>>>>>> parent of de53fed6 (flask报销系统的分页及bootstrap)

from app.forms import ReimbursementForm

@login_required
@app.route('/reimbursement', methods=['GET', 'POST'])
def reimbursement():
    form = ReimbursementForm()
    if form.validate_on_submit():
        record = Reimbursement(source=form.source.data, name=form.name.data,qty=float(form.qty.data),total=float(form.total.data))
        db.session.add(record)
        db.session.commit()
        #aaaa.append(form.source.data)
        return redirect(url_for('index'))
        #flash('Congratulations, you are now a registered user!')
        #return redirect(url_for('login'))
<<<<<<< HEAD
<<<<<<< HEAD
    return render_template('reimbursement.html', title='采购记录', form=form)

from app.forms import RegistrationForm,EditProfileForm, EmptyForm


@app.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot follow yourself!')
            return redirect(url_for('user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash('You are following {}!'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))


@app.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot unfollow yourself!')
            return redirect(url_for('user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash('You are not following {}.'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))
=======
    return render_template('reimbursement.html', title='采购记录', form=form)
>>>>>>> parent of de53fed6 (flask报销系统的分页及bootstrap)
=======
    return render_template('reimbursement.html', title='采购记录', form=form)
>>>>>>> parent of de53fed6 (flask报销系统的分页及bootstrap)
