from app.main.util import load_model

ml_model = load_model.load_house_prices_model('')


def predict_price(data):
    try:
        price = ml_model.predict(data)
        response_object = {
            'status': 'success',
            'message': 'Successfully predicted.',
            'predicted price': price
        }
        return response_object, 201

    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401

