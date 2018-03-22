from collections import OrderedDict
from flask import Flask
from flask_restplus import Api, Resource

import mymodel, mystorage

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
            
		
if __name__ == '__main__':
    app.run(debug=True)