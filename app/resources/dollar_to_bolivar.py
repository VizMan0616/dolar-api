from flask_restful import Resource, reqparse, abort, marshal_with
from ..common.constants import RESOURCE_FIELDS
from ..common.utils import *
from ..models import DollarModel


class DollarBolivar(Resource):
    @marshal_with(RESOURCE_FIELDS)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('usd', type=float, default=1.0)

        args = parser.parse_args()

        return DollarModel(usd=args['usd'], ves=usd_to_ves(args['usd']))
