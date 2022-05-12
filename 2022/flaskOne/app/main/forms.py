from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,FloatField,PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, InputRequired,DataRequired, Email, EqualTo, Length

# Flask表单验证组件WTForms
class ReimbursementForm(FlaskForm):
    # 应对templates 下的模板，模板不需要按字段配置
    source = StringField('Source', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    qty = FloatField('Qty', validators=[DataRequired()])
    total = FloatField('Total', validators=[InputRequired()],default=0)
    type = SelectField('type', validators=[DataRequired()],default=1)
    send = SelectField('send', validators=[DataRequired()],default=1)
    #date = db.Column(db.Date, index=True, default=datetime.utcnow)

    submit = SubmitField('Reimbursement')

    def __init__(self, *args, **kwargs):
        super(ReimbursementForm, self).__init__(*args, **kwargs)
        self.type.choices = ['无票','电子','纸质']
        self.send.choices = ['未索要','已索要','已发送']
            #[(category.id, category.name)
            #                     for category in Category.query.order_by(Category.name).all()]
