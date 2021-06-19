from flask_restful import Resource, reqparse, abort, marshal_with
from ..common.constants import RESOURCE_FIELDS
from ..common.utils import *
from ..models import DollarModel


class BolivarsDollar(Resource):
    @marshal_with(RESOURCE_FIELDS)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'bolivars', type=float, help='Se requiere la cantidades de bolivares a convertir', required=True)

        args = parser.parse_args()

        return DollarModel(dollar=bolivars_to_bucks(args['bolivars']), bolivar=args['bolivars'])
