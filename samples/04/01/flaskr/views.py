from flask import request, redirect, url_for, render_template, flash
from flaskr import app, db
from flaskr.models import Entry

@app.route('/')
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    entry = Entry(
            title=request.form['title'],
            text=request.form['text']
            )
    db.session.add(entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/users/')
def user_list():
    return 'list users'

@app.route('/users/<int:user_id>/')
def user_detail(user_id):
    return 'detail user ' + str(user_id)

@app.route('/users/<int:user_id>/edit/', methods=['GET', 'POST'])
def user_edit(user_id):
    return 'edit user ' + str(user_id)

@app.route('/users/create/', methods=['GET', 'POST'])
def user_create():
    return 'create a new user'

@app.route('/users/<int:user_id>/delete/', methods=['DELETE'])
def user_delete(user_id):
    return NotImplementedError('DELETE')

