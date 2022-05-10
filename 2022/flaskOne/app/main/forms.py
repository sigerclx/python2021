from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length


class ReimbursementForm(FlaskForm):
    # 应对templates 下的模板，模板不需要按字段配置
    source = StringField('Source', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    qty = StringField('Qty', validators=[DataRequired()])
    total = StringField('Total', validators=[DataRequired()])

    submit = SubmitField('Reimbursement')
