from flask import Blueprint, render_template, request, redirect, \
        url_for, flash, session, abort, jsonify
from flaskr.models import User, db
from flaskr.frontend import login_required
from flaskr.forms import LoginForm


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/')
@login_required
def user_list():
    users = User.query.all()
    return render_template('user/list.html', users=users)

@bp.route('/<int:user_id>/')
@login_required
def user_detail(user_id):
    user = User.query.get(user_id)
    return render_template('user/detail.html', user=user)

@bp.route('/<int:user_id>/edit/', methods=['GET', 'POST'])
@login_required
def user_edit(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404)
    if request.method == 'POST':
        user.name=request.form['name']
        user.email=request.form['email']
        if request.form['password']:
            user.password=request.form['password']
        #db.session.add(user)
        db.session.commit()
        return redirect(url_for('.user_detail', user_id=user_id))
    return render_template('user/edit.html', user=user)

@bp.route('/create/', methods=['GET', 'POST'])
@login_required
def user_create():
    if request.method == 'POST':
        user = User(name=request.form['name'],
                    email=request.form['email'], 
                    password=request.form['password'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.user_list'))
    return render_template('user/edit.html')

@bp.route('/<int:user_id>/delete/', methods=['DELETE'])
def user_delete(user_id):
    user = User.query.get(user_id)
    if user is None:
        response = jsonify({'status': 'Not Found'})
        response.status_code = 404
        return response
    db.session.delete(user)
    db.session.commit()
    return jsonify({'status': 'OK'})


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user, authenticated = User.authenticate(db.session.query, 
                form.email.data, form.password.data)
        if authenticated:
            session['user_id'] = user.id
            flash('You were logged in')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password')
    return render_template('login.html', form=form)

@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You were logged out')
    return redirect(url_for('index'))



