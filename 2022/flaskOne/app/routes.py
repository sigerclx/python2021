from flask import render_template
from datetime import datetime
import math
from app import app,baseDict
from app.forms import EmptyForm
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
from flask_login import current_user


from flask import request




from app import db



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