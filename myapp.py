from flask import Flask, jsonify
from os import getenv

def create_app():
    app = Flask(__name__)

    @app.route('/ping') # the extension of the url
    def ping():
        return jsonify(ping ='pong alex')

    return app

	#def test_api_ping(client):
#res = client.get(url_for('api.ping'))
#assert res.json == {'ping': 'pong'}

if __name__ == '__main__':
    app = create_app()
	
    port_str = getenv('PORT', '5000')
    port_int = int(port_str)
    assert port_str == str(port_int)
	
    app.run(port=port_int, host='0.0.0.0', threaded=True)