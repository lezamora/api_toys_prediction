from app.main.util.load_model import load_house_prices_model
import pandas as pd

ml_model = load_house_prices_model('C:\\Repositorios\\api_toys_prediction\\app\\main\\model\\xbregresor2019_02_18__14_41.joblib')


def predict_price(data):
    data = pd.DataFrame([data], columns=['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
                                         'waterfront', 'view', 'condition', 'grade', 'sqft_above',
                                         'sqft_basement', 'yr_built', 'zipcode', 'lat', 'long', 'sqft_living15',
                                         'sqft_lot15', 'house_age', 'renovated'])
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

