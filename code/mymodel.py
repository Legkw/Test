from flask_restplus import fields

# TODO: use the inherit fun ctionality of flask_restplus
# https://flask-restplus.readthedocs.io/en/0.8.2/documenting.html#polymorphism-with-api-inherit

model_neo = {
    'date_from': fields.Date(required=True),
	'date_till': fields.Date(required=True)
}

model_idi = model_neo.copy()
model_idi.update({
	'id': fields.Integer(readOnly=True, min=0)
})

class absence(object):
    def __init__(self, date_from, date_till):
        self.date_from = date_from
        self.date_till = date_till
        self.id = None