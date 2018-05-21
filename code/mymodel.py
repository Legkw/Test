from flask_restplus import fields

model_neo = {
    'date_from': fields.Date(required=True),
	'date_till': fields.Date(required=True)
}

model_idi = model_neo.copy()
model_idi.update({
	'id': fields.Integer(readOnly=True)
})

class absence(object):
    def __init__(self, date_from, date_till):
        self.date_from = date_from
        self.date_till = date_till
        self.id = None