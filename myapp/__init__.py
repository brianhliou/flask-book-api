from flask import Flask, jsonify, request
from .views.user_views import user_blueprint
from .views.book_views import book_blueprint
from .config import Config
from .log import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.register_blueprint(user_blueprint)
    app.register_blueprint(book_blueprint)
    
    @app.before_request
    def log_request_info():
        logging.debug('Headers: %s', request.headers)
        logging.debug('Body: %s', request.get_data())

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'error': 'Not Found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal Server Error'}), 500


    return app