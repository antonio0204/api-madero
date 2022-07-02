from flask import request
from flask_restplus import Resource, reqparse

from ..util.dto import TerrenoDto
from ..service.terrenos_service import get

api = TerrenoDto.api
_terreno = TerrenoDto.terreno

# GET /price-m2/zip-codes/{zip_code}/aggregate/{max|min|avg}?construction_type={1-7}

parser = reqparse.RequestParser()
parser.add_argument('construction_type', type=int, help='Construction type', required=True)


@api.route('/<string:zip_code>/aggregate/<string:aggregate>')
@api.param('zip_code', 'ZIP code')
@api.param('aggregate', 'Type aggregate')
class TerrenoList(Resource):
    @api.doc('Terrenos')
    @api.marshal_list_with(_terreno, envelope='data')
    def get(self, zip_code, aggregate):

        aggregates = ('max', 'min', 'avg')

        if aggregate not in aggregates:
            response_object = {
                'status': 'fail',
                'message': 'The given aggregate is not available. Options: max, min, avg'
            }

            return response_object, 201

        construction_types = {
            1: 'Áreas verdes',
            2: 'Centro de barrio',
            3: 'Equipamiento',
            4: 'Habitacional',
            5: 'Habitacional y comercial',
            6: 'Industrial',
            7: 'Sin Zonificación'
        }

        construction_type = int(request.args.get('construction_type'))

        if construction_type not in construction_types:
            response_object = {
                'status': 'fail',
                'message': 'The given construction type is not available. Options: 1, 2, 3, 4, 5, 6, 7'
            }

            return response_object, 201

        print(zip_code, aggregate, construction_type)
        return get(aggregate, zip_code, construction_types[construction_type])
