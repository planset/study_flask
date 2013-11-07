================
Flask quickstart
================
:参照: `クイックスタート — flask-docs-ja 0.10-dev documentation <https://flask-docs-ja.readthedocs.org/en/latest/quickstart/#quickstart>`_

A Minimal Application: OK

Debug Mode
===========
::

    app.debug = True
    app.run()

or::

    app.run(debug=True)

Routing
=======
::

    @app.route('/')
    def index():
        return 'Index Page'

    @app.route('/hello')
    def hello():
        return 'Hello World'

Variable Rules
==============
::

    @app.route('/user/<username>')
    def show_user_profile(username):
        return 'User %s' % username

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        return 'Post %d' % post_id

デフォルトでは以下の型の指定が可能

:int: 整数
:float: 小数
:path: URLパス


URL Building
============
@app.routeで追加したルートはurl_forでURLを取得することができる。::

    >>> from flask import Flask, url_for
    >>> app = Flask(__name__)
    >>> @app.route('/')
    ... def index(): pass
    ...
    >>> @app.route('/login')
    ... def login(): pass
    ...
    >>> @app.route('/user/<username>')
    ... def profile(username): pass
    ...
    >>> with app.test_request_context():
    ...  print url_for('index')
    ...  print url_for('login')
    ...  print url_for('login', next='/')
    ...  print url_for('profile', username='John Doe')
    ...
    /
    /login
    /login?next=/
    /user/John%20Doe


HTTP Methods
============
::

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            do_the_login()
        else:
            show_the_login_form()


* GET, HEAD, POST, PUT, DELETE, OPTIONS


Static Files 
============
::

    url_for('static', filename='style.css')


Rendering Templates
====================
サンプルはFlaskrでOK


The Request Object
==================
サンプルはFlaskrでOK


File Uploads
============
form側を enctype="multipart/form-data"とした上で、
request.files['name']でアクセスすることができる。::

    from flask import request
    from werkzeug ipmort secure_filename

    @app.route('/upload', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            f = request.files['the_file']
            f.save('/var/www/uploads/' + secure_filename(f.filename))

Cookies
=========
get::

    request.cookies.get('username')

set::

    from flask import make_response

    @app.route('/')
    def index():
        resp = make_response(render_template(...))
        resp.set_cookie('username', 'the username')
        return resp

Redirect and Errors
===================
::

    from flask import abort, redirect, url_for, render_template

    @app.route('/')
    def index():
        return redirect(url_for('login'))

    @app.route('/login')
    def login():
        abort(401)
        this_is_never_executed()

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html'), 404


Message Flashing
==================
サンプルはFlaskrでOK


Logging
========
のちほど


Hooking in WSGI Middlewares
===========================
のちほど


Deploying to a Web Server
=========================
のちほど



