import os
import joblib

def load_house_prices_model(model_path):
    if os.path.exists(model_path):
        loaded_model = joblib.load(model_path)
    else:
        loaded_model = None
    return loaded_model
