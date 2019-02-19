from ..util.load_model import load_house_prices_model
from ..config import model_path, columns
import pandas as pd

ml_model = load_house_prices_model(model_path)


def predict_price(data):
    data = pd.DataFrame([data], columns=columns)
    try:
        response_object = {
            'status': 'success',
            'message': 'Successfully predicted.',
            'predicted price': float(ml_model.predict(data))
        }
        return response_object, 201

    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.',
            'error': '{}'.format(e)
        }
        return response_object, 400

