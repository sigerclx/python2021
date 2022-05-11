from flask import render_template, redirect, url_for
import math
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, jsonify, current_app
from app import db,baseDict
from app.home import bp
from app.models import User,Reimbursement
from app.home.forms import EmptyForm,EditProfileForm
from flask_login import login_required

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    reimbursements = Reimbursement.query.order_by(Reimbursement.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    # 按记录数计算总页数，向上取整
    Allpages = math.ceil(int(reimbursements.total) /  current_app.config['POSTS_PER_PAGE'])
    first_url = url_for('home.index', baseDict=baseDict, page=1)
    next_url = url_for('home.index', baseDict=baseDict,page=reimbursements.next_num) \
        if reimbursements.has_next else None
    prev_url = url_for('home.index',baseDict=baseDict, page=reimbursements.prev_num) \
        if reimbursements.has_prev else None
    # baseDict=baseDict 是否可以不在这传递？
    last_url = url_for('home.index', page=Allpages)

    return render_template('home/index.html', baseDict=baseDict, reimbursements=reimbursements.items,
                           first_url=first_url,next_url=next_url, prev_url=prev_url,last_url=last_url)

from flask_login import current_user

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    #return render_template('user.html', user=user, posts=posts)
    form = EmptyForm()
    return render_template('/home/user.html', user=user, posts=posts, form=form)



@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        #current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('home.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('/home/edit_profile.html', title='Edit Profile',form=form)




@bp.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('home.index'))
        if user == current_user:
            flash('You cannot follow yourself!')
            return redirect(url_for('home.user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash('You are following {}!'.format(username))
        return redirect(url_for('home.user', username=username))
    else:
        return redirect(url_for('home.index'))


@bp.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('home.index'))
        if user == current_user:
            flash('You cannot unfollow yourself!')
            return redirect(url_for('home.user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash('You are not following {}.'.format(username))
        return redirect(url_for('home.user', username=username))
    else:
        return redirect(url_for('home.index'))