from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
#from flask_babel import _
from app import db
from app.main import bp
from app.models import Reimbursement
#from app.auth.email import send_password_reset_email
from flask_login import login_required
from app.main.forms import ReimbursementForm


@bp.route('/reimbursement', methods=['GET', 'POST'])
@login_required
def reimbursement():
    form = ReimbursementForm()
    if form.validate_on_submit():
        record = Reimbursement(source=form.source.data, name=form.name.data,qty=form.qty.data, \
                               total=form.total.data,type=form.type.data,send=form.send.data)
        db.session.add(record)
        db.session.commit()
        #aaaa.append(form.source.data)
        return redirect(url_for('home.index'))
        #flash('Congratulations, you are now a registered user!')
        #return redirect(url_for('login'))
    return render_template('main/reimbursement.html', title='采购记录', form=form)