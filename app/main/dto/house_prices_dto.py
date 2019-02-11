from flask_restplus import Namespace, fields


class HousePricesDto:
    api = Namespace('house_prices', description='data set about house prices')
    house_prices = api.model('house_prices', {
        'price': fields.String(required=True, description='Predicted price'),
    })