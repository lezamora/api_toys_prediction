from flask import request
from flask_restplus import Resource

from ..dto.house_prices_dto import HousePricesDto
from ..service.house_prices_service import predict_price

api = HousePricesDto.api
_house_prices = HousePricesDto.house_prices


@api.route('')
class PredictPrice(Resource):
    @api.expect(_house_prices, validate=True)
    @api.response(201, 'Price predicted successfully.')
    @api.response(400, 'Some error occurred.')
    @api.doc('predict a house prices')
    def post(self):
        """
        Predict a House Prices

        * Use this method to predict house prices. Returns the next body:

         ```
        {
          'status': 'success',
          'message': 'Successfully predicted',
          'predicted price': 'Price predicted'
        }
        ```

        """
        data = request.json
        return predict_price(data=data)



