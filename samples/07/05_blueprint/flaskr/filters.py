# -*- coding: utf-8 -*-


def init_app(app):
    app.jinja_env.filters['datetime'] = do_datetime

def do_datetime(dt, format='%Y-%m-%d @ %H:%M'):
    formatted = ''
    if dt is not None:
        formatted = dt.strftime(format)
    return formatted

