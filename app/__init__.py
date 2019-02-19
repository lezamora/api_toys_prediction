from flask_restplus import Api
from flask import Blueprint

from .main.controller.house_prices_controller import api as house_prices_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='API TOYS PREDICTION',
          version='1.0',
          description='A flask api for predictions'
          )


api.add_namespace(house_prices_ns)
