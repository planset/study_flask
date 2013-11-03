
概要・予定
==========






内容
====
* Flaskチュートリアル  45分
    * http://flask.pocoo.org/docs/tutorial/
    * Flask Quickstartに書かれている内容は、チュートリアルの説明で行う。
	
* 休憩 15分

* Flaskを使いこなす1    40分
    * DB周りをSQLAlchemyにする。http://methane.github.io/flask-handson/flaskr.html#step-0 参照	20分
    * Logging	10分
    * Testing Flask Applications  10分

* 実稼働環境で動かす	20分
    * apache: mod_wsgi, nginx:wsgi(wsgi module)
    * wsgi server: uWSGI, gunicorn
    * PaaS: heroku, dotCloud <- 無料か？
    * もっと楽な方法が良いのだが・・・

* 休憩 15分

* Flaskを使いこなす2    30分
    * Flaskを使った開発パターン　`Patterns for Flask — Flask 0.10.1 documentation <http://flask.pocoo.org/docs/patterns/>`_
	* Larger Applications
	* Application Factories
	* Uploading Files
	* View Decorators
	* Form Validation with WTForms
	* Adding a favicon
	* Celery Based Background Tasks
	* これらを盛り込んだハンズオン・・・は厳しいかな。説明だけかな。

* おすすめプラグイン 5分
    * Flask-WTF(wtforms) 
    * Flask-SQLAlchemy(SQLAlchemy) 
    * Flask-DebugToolbar
    * Flask-Security
        * Flask-Login
        * Flask-Mail
        * Flask-Principal
        * Flask-Script
        * Flask-WTF
        * itsdangerous
        * passlib
    * Flask-Assets
	
* 参考になるサンプルアプリ 2分
    * `flask/flask_website at website · mitsuhiko/flask <https://github.com/mitsuhiko/flask/tree/website/flask_website>`_
    * `Python+FlaskなwebアプリをJenkinsでウイーン - Qiita [キータ] <http://qiita.com/smellman/items/49811c8cf3cda6b8a16d>`_


備考
====
* なるべく公式ドキュメントを使いながらやりたい。
* チュートリアルを開始するためのひな形を用意（git, zip 。完成品は公式にある。



