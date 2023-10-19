import requests
import requests_mock

from hello_plumber.consume import RApiConsumer

def test_consume():
    with requests_mock.mock() as m:
        expected_data = {'msg': ["The message is: 'wait_for_api'"]}  # otherwise will complain about no mock address
        m.get('http://localhost:8000/echo?msg=wait_for_api', json=expected_data)

        # Now, run the code you want to test
        with RApiConsumer(port=8000) as api:
            response = requests.get('http://localhost:8000/echo?msg=wait_for_api') # does not make a real call -> but uses the mock set up

            assert response.status_code == 200
            data = response.json()
            assert data == expected_data