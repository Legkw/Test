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
	
    port_str = getenv('PORT', '5000')
    port_int = int(port_str)
    assert port_str == str(port_int)
	
    app.run(port=port_int, host='0.0.0.0', threaded=True)