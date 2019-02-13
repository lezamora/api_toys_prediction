from flask import request
from flask_restplus import Resource

from ..dto.house_prices_dto import HousePricesDto
from ..service.house_prices_service import predict_price

api = HousePricesDto.api
_house_prices = HousePricesDto.house_prices


@api.route('/')
class PredictPrice(Resource):
    @api.expect(_house_prices, validate=True)
    @api.response(201, 'Price predicted successfully.')
    @api.doc('predict a house prices')
    def post(self):
        """Predict a House Prices """
        data = request.json
        return predict_price(data=data)



