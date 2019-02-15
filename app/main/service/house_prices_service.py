from ..util.load_model import load_house_prices_model

ml_model = load_house_prices_model('C:\\Repositorios\\api_toys_prediction\\app\\main\\model\\xbregresor2019_02_14__15_56.joblib')


def predict_price(data):
    try:
        response_object = {
            'status': 'success',
            'message': 'Successfully predicted.',
            'predicted price': float(ml_model.predict(list(data.values()))[0])
        }
        return response_object, 201

    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 400

