==================
SQLAlchemyについて
==================
* SQL Toolkit & Object Relational Mapper

使用例
======
定義
----
チュートリアルではschema.sqlを使ってデータベースを生成していましたが、
SQLAlchemyを使うとデータベースの定義と生成はこんな感じになります。::

    class Entry(db.Model):
        __tablename__ = 'entries'
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.Text(), nullable=False)
        text = db.Column(db.Text(), nullable=False)

    def init_db():
        db.create_all()

select
------
::

    SELECT * FROM entries WHERE id > 10 ORDER BY id DESC;
      ↓
    Entry.query.filter(Entry.id > 10).order_by(Entry.id.desc()).all()

    under_20 = Entry.query.filter(User.age < 20)
    under_20_and_male = under_20.filter(User.gendar == 'male')

insert
------
::

    INSERT INTO entries(title, text) VALUES ('title', 'text');
      ↓
    entry = Entry()
    entry.title = 'title'
    entry.text = 'text'
    db.session.add(entry)
    db.session.commit()

update
------
::

    UPDATE entries SET title = 'title2' WHERE id = 1;
      ↓
    entry = Entry.query.filter(Entry.id == 1).first()
    entry.title = 'title2'
    db.session.add(entry)
    db.session.commit()

delete
------
::

    DELETE FROM entries WHERE id = 3;
      ↓
    entry = Entry.query.filter(Entry.id == 3).first()
    db.session.delete(entry)
    db.session.commit()


FlaskでSQLAlchemyを使う
-----------------------
* そのまま使ってもいい
* extensionにFlask-SQLAlchemyというのがあるので今回はそれを利用
