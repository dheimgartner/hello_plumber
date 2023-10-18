import requests
import requests_mock

from hello_plumber.consume import RApiConsumer

def test_consume():
    with requests_mock.mock() as m:
        expected_data = {'msg': ["The message is: 'hello'"]}
        m.get('http://localhost:8000/echo?msg=hello', json=expected_data)

        # Now, run the code you want to test
        with RApiConsumer(port=8000) as api:
            response = requests.get('http://localhost:8000/echo?msg=hello') # does not make a real call -> but uses the mock set up

            assert response.status_code == 200
            data = response.json()
            assert data == expected_data