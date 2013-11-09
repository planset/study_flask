import os
import logging
from logging.handlers import RotatingFileHandler

def setup_log(app):
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    )
    debug_log = os.path.join(app.root_path, 'logs/debug.log')
        
    debug_file_handler = RotatingFileHandler(
        debug_log, maxBytes=100000, backupCount=10
    )
        
    debug_file_handler.setLevel(logging.INFO)
    debug_file_handler.setFormatter(formatter)
    app.logger.addHandler(debug_file_handler)
        
    error_log = os.path.join(app.root_path, 'logs/error.log')
    error_file_handler = RotatingFileHandler(
        error_log, maxBytes=100000, backupCount=10
    )    
    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)

    app.logger.setLevel(logging.DEBUG)

