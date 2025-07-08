from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField("Your Name", validators=[DataRequired()])
    message = TextAreaField("Your Message", validators=[DataRequired()])
