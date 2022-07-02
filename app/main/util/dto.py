from flask_restplus import Namespace, fields


class TerrenoDto:
    api = Namespace('terreno', description='Operaciones sobre terrenos')

    payload = api.model('payload', {
        'type': fields.String(readonly=True, description='Type'),
        'price_unit': fields.Float(readonly=True, description='Price unit'),
        'price_unit_construction': fields.Float(readonly=True, description="Price unit construction"),
        'elements': fields.Integer(readonly=True, description="elements"),
    })

    terreno = api.model('terreno', {
        'status': fields.Boolean(required=False, description='Estado'),
        'payload': fields.Nested(payload, description='Payload')
    })
