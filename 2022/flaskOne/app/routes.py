from flask import render_template
from datetime import datetime
import math
from app import app,baseDict
from app.forms import LoginForm
from flask_login import login_required
from app.models import User,Reimbursement

@app.route('/')
@app.route('/index')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    reimbursements = Reimbursement.query.order_by(Reimbursement.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    # 按记录数计算总页数，向上取整
    Allpages = math.ceil(int(reimbursements.total) /  app.config['POSTS_PER_PAGE'])
    first_url = url_for('index', baseDict=baseDict, page=1)
    next_url = url_for('index', baseDict=baseDict,page=reimbursements.next_num) \
        if reimbursements.has_next else None
    prev_url = url_for('index',baseDict=baseDict, page=reimbursements.prev_num) \
        if reimbursements.has_prev else None
    # baseDict=baseDict 是否可以不在这传递？
    last_url = url_for('index', page=Allpages)

    return render_template('index.html', baseDict=baseDict, reimbursements=reimbursements.items,
                           first_url=first_url,next_url=next_url, prev_url=prev_url,last_url=last_url)

from flask import render_template, flash, redirect,url_for
from flask_login import current_user, login_user
from flask_login import logout_user




from flask import request
from werkzeug.urls import url_parse




from app import db
# from app.forms import RegistrationForm,EditProfileForm, EmptyForm
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login'))
#         login_user(user, remember=form.remember_me.data)
#         next_page = request.args.get('next')
#         if not next_page or url_parse(next_page).netloc != '':
#             next_page = url_for('index')
#         return redirect(next_page)
#
#     return render_template('login.html', title='Sign In', form=form)

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)

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
    #return render_template('user.html', user=user, posts=posts)
    form = EmptyForm()
    return render_template('user.html', user=user, posts=posts, form=form)



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
    return render_template('reimbursement.html', title='采购记录', form=form)


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