from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Length
from .models import Item


class ItemForm(Form):
	title = StringField('title', validators = [DataRequired()])
	course = RadioField('course', choices=[('Appetizer', 'Appetizer'),('Entree', 'Entree'), ('Dessert', 'Dessert'), ('Beverage', 'Beverage')])
	price = StringField('price', validators = [DataRequired()])
	description = TextAreaField('description', validators = [Length(min=0, max=500)])


class EditForm(Form):
    title = StringField('title', validators = [DataRequired()])
    course = RadioField('course', choices=[('Appetizer', 'Appetizer'),('Entree', 'Entree'), ('Dessert', 'Dessert'), ('Beverage', 'Beverage')])
    price = StringField('price', validators = [DataRequired()])
    description = TextAreaField('description', validators = [Length(min=0, max=500)])

   

def validate(self):
        if not Form.validate(self):
            return False
        return True

