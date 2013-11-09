from flask import Blueprint, current_app, render_template, request, redirect, \
        url_for, flash
from flaskr.models import Entry, db

bp = Blueprint('entries', __name__, url_prefix='/entries')


@bp.route('/')
def show_entries():
    current_app.logger.debug('debug')
    current_app.logger.info('info')
    current_app.logger.warning('warning')
    current_app.logger.error('error')
    current_app.logger.critical('critical')
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('show_entries.html', entries=entries)

@bp.route('/add', methods=['POST'])
def add_entry():
    entry = Entry(
            title=request.form['title'],
            text=request.form['text']
            )
    db.session.add(entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('.show_entries'))

