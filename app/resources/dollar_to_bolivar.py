from flask_restful import Resource, reqparse, abort, marshal_with
from ..common.constants import RESOURCE_FIELDS
from ..common.utils import *
from ..models import DollarModel


class DollarBolivar(Resource):
    @marshal_with(RESOURCE_FIELDS)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('dollars', type=float, default=1.0)

        args = parser.parse_args()

        return DollarModel(dollar=args['dollars'], bolivar=bucks_to_bolivar(args['dollars']))
