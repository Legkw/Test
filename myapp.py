from flask import Flask, jsonify
from os import getenv

def create_app():
    app = Flask(__name__)

    @app.route('/ping')
    def ping():
        return jsonify(ping='pong')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=getenv('PORT', '5000'), host='0.0.0.0', threaded=True)