from flask import Flask
from flask_restplus import Api, Resource
from os import getenv
import mymodel, mystorage

		
def create_app():    
    app = Flask(__name__)
    api = Api(app)
    model_neo = api.model('model_neo', mymodel.model_neo)
    model_idi = api.model('model_idi', mymodel.model_idi)

    storage = mystorage.inmemory()

    @api.route('/')
    class Items(Resource):
        @api.doc('create_item')
        @api.expect(model_neo)
        @api.marshal_with(model_idi, code=201)
        def post(self, **kwargs):
            item = mymodel.absence(**api.payload)
            storage.add(item)
            '''Create a new item'''
            return item
		
    @api.route('/<int:id>')
    @api.param('id', 'item identifier')
    class Item(Resource):
        @api.marshal_with(model_idi)
        def get(self, id):
            try: 
                return storage.get(id)
            except (KeyError):
                api.abort(404, "Item not found")
                
        @api.response(200, "Deleted")
        def delete(self, id):
            try:
                storage.delete(id)
            except (KeyError):
                api.abort(404, "Item not found")
    
    return app

if __name__ == '__main__':
    app = create_app()
	
    port_str = getenv('PORT', '5000')
    port_int = int(port_str)
    assert port_str == str(port_int)
	
    app.run(port=port_int, host='0.0.0.0', threaded=True)