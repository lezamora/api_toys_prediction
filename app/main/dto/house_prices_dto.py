from flask_restplus import Namespace, fields


class HousePricesDto:
    api = Namespace('house_prices', description='data set about house prices')
    house_prices = api.model('house_prices', {
        'sqft_living': fields.Integer(required=True, description='Measurement of house in square foot'),
        'grade': fields.Integer(required=True, description='Overall grade given to the housing unit(1-11)'),
        'sqft_above': fields.Integer(required=True, description='Square footage of house apart from basement'),
        'sqft_living15': fields.Integer(required=True, description='Living room area in 2015'),
        'bathrooms': fields.Integer(required=True, description='Number of bathrooms in a bedroom of a house'),
        'view': fields.Integer(required=True, description='If the house has been viewed or not 0 means no 1 means yes'),
        'sqft_basement': fields.Integer(required=True, description='Square footage of the basement of the housee'),
        'bedrooms': fields.Integer(required=True, description='Number of bedrooms in a house'),
        'lat': fields.Float(required=True, description='Latitude of the location of the house'),

        'waterfront': fields.Integer(required=True, description='Determines whether a house has a view to waterfront\
                                                            0 means no 1 means yes.'),
        'floors': fields.Integer(required=True, description='Total floors means levels of house'),
        'renovated': fields.Integer(required=True, description='If the house has been renovated or not\
                                                                0 means no 1 means yes'),
        'sqft_lot': fields.Integer(required=True, description='LotSize area in 2015'),
        'sqft_lot15': fields.Integer(required=True, description='LotSize area'),
        'yr_built': fields.Integer(required=True, description='Date of building of the house'),
        'condition': fields.Integer(required=True, description='Overall condition of a house on a scale of 1 to 5'),
        'long': fields.Float(required=True, description='Longitude of the location of the house'),
        'zipcode': fields.Integer(required=True, description='Zipcode of the location of the house'),
        'house_age': fields.Integer(required=True, description='Antique of the house')
    })


