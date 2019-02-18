import unittest
import json

from app.test.base import BaseTestCase


def predict_price(self):
    return self.client.post(
        '/house_prices/',
        data=json.dumps(dict(
            sqft_living=1180,
            grade=7,
            sqft_above=1180,
            sqft_living15=1340,
            bathrooms=1,
            view=1,
            sqft_basement=0,
            bedrooms=3,
            lat=47.5112,
            waterfront=0,
            floors=1,
            renovated=0,
            sqft_lot=5650,
            sqft_lot15=5650,
            yr_built=1955,
            condition=3,
            long=-122.257,
            zipcode=98178,
            house_age=59
        )),
        content_type='application/json'
    )


class TestHousePrices(BaseTestCase):
    def test_predict_price(self):
        with self.client:
            response = predict_price(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully predicted.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
