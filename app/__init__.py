from flask_restplus import Api
from flask import Blueprint

from .main.controller.house_prices_controller import api as house_prices_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(house_prices_ns)
