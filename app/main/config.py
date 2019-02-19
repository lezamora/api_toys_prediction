import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    MODEL_PATH = 'C:\\Repositorios\\api_toys_prediction\\app\\main\\model\\xbregresor2019_02_18__14_41.joblib'
    COLUMNS_ORDER = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition',
                     'grade', 'sqft_above', 'sqft_basement', 'yr_built', 'zipcode', 'lat', 'long', 'sqft_living15',
                     'sqft_lot15', 'house_age', 'renovated']
    LOG_CONFIG_PATH = 'C:\\Repositorios\\api_toys_prediction\\logging.ini'


class DevelopmentConfig(Config):
    # Flask settings
    SERVER_NAME = 'localhost:7070'
    DEBUG = True  # Do not use debug mode in production

    # Flask-Restplus settings
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False


config_by_name = dict(
    dev=DevelopmentConfig
)

model_path = Config.MODEL_PATH
columns = Config.COLUMNS_ORDER
log_path = Config.LOG_CONFIG_PATH
