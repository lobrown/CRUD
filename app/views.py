from flask import render_template, flash, redirect, session, url_for, request
from app import app, db, models
from .forms import EditForm, ItemForm
from .models import Item



#@app.errorhandler(404)
#def not_found_error(error):
#    return render_template('404.html'), 404


#@app.errorhandler(500)
#def internal_error(error):
#    db.session.rollback()
#    return render_template('500.html'), 500



@app.route('/', methods = ['GET', 'POST'])
@app.route('/index')
def index():
	item = ItemForm()
	items = models.Item.query.all()
	return render_template('index.html', items = items)




@app.route('/edit/<title>', methods=['GET', 'POST'])
def edit(title):
	item = Item.query.filter_by(title=title).first()
	form = EditForm(obj=item)
	if form.validate_on_submit():
		item.title = form.title.data
		item.course = form.course.data
		item.price = form.price.data
		item.description = form.description.data

		db.session.add(item)
		db.session.commit()
		flash('Item has been updated')
		return redirect(url_for('index'))
	return render_template('edit.html', form=form, item=item)



@app.route('/new', methods=['GET', 'POST'])
def new():
	form=ItemForm()

	if form.validate_on_submit():
		item = models.Item(title=form.title.data, course=form.course.data, price=form.price.data, description = form.description.data)
		db.session.add(item)
		db.session.commit()
		flash('New Item has been created')
		return redirect(url_for('index'))
	return render_template('new.html', form=form)




@app.route('/delete/<title>', methods=['GET', 'POST'])
def delete(title):
	item = Item.query.filter_by(title=title).first()
	db.session.delete(item)
	db.session.commit()
	flash('This item has been deleted.')
	return redirect(url_for('index'))



