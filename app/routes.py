from flask import Blueprint
from flask_restful import Api

from .resources.dollar_to_bolivar import DollarBolivar
from .resources.bolivars_to_dollar import BolivarsDollar

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

api.add_resource(DollarBolivar, '/dollar')
api.add_resource(BolivarsDollar, '/bolivar')
