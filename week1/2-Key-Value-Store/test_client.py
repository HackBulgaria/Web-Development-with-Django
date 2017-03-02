import uuid
import re
import requests
import unittest


UUID4_REGEX = re.compile('([a-zA-Z]|[0-9]){8}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){12}')
BASE_URL = 'http://localhost:8000/storage'
CREATE_USER_URL = BASE_URL + '/create-user/'
STORE_KEY_URL = BASE_URL + '/{identifier}/'
GET_KEY_URL = BASE_URL + '/{identifier}/{key}/'
DELETE_KEY_URL = BASE_URL + '/{identifier}/{key}/'
TIMEOUT = 2


def is_uuid4(value):
    return UUID4_REGEX.match(value)


def create_user():
    response = requests.get(CREATE_USER_URL, timeout=TIMEOUT)
    return response


def store_key(identifier, key, value):
    url = STORE_KEY_URL.format(identifier=identifier)
    data = {'key': key,
            'value': value}
    response = requests.post(url, json=data, timeout=TIMEOUT)

    return response


def get_key(identifier, key):
    url = GET_KEY_URL.format(identifier=identifier, key=key)
    response = requests.get(url, timeout=TIMEOUT)

    return response


def delete_key(identifier, key):
    url = DELETE_KEY_URL.format(identifier=identifier, key=key)
    response = requests.delete(url, timeout=TIMEOUT)

    return response


class KeyValueStoreTests(unittest.TestCase):
    def test_create_user_is_successful(self):
        response = create_user()

        self.assertEqual(200, response.status_code, 'Response should be 200 OK')
        self.assertEqual('application/json', response.headers['Content-Type'], 'Content-Type should be application/json')

        data = response.json()

        self.assertIn('identifier', data, 'Data should have identifier key')
        self.assertTrue(is_uuid4(data['identifier']), 'identifier should be a valid uuid')

    def test_store_key_is_successful(self):
        response = create_user()
        identifier = response.json()['identifier']

        response = store_key(identifier, key='foo', value='bar')
        self.assertEqual(201, response.status_code)

    def test_store_key_for_non_existing_user_returns_404(self):
        identifier = str(uuid.uuid4())
        response = store_key(identifier, key='foo', value='bar')
        self.assertEqual(404, response.status_code)

    def test_store_key_for_non_uuid4_identifier_returns_404(self):
        identifier = 'asdf'
        response = store_key(identifier, key='foo', value='bar')
        self.assertEqual(404, response.status_code)

    def test_get_key_after_storing_it_is_successful(self):
        response = create_user()
        identifier = response.json()['identifier']

        store_key(identifier, key='foo', value='bar')
        response = get_key(identifier, 'foo')

        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.headers['Content-Type'], 'Content-Type should be application/json')

        data = response.json()

        self.assertEqual('bar', data['value'])

    def test_get_key_after_overwriting_it_is_successful(self):
        response = create_user()
        identifier = response.json()['identifier']

        store_key(identifier, key='foo', value='bar')
        store_key(identifier, key='foo', value='baz')
        response = get_key(identifier, 'foo')

        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.headers['Content-Type'], 'Content-Type should be application/json')

        data = response.json()

        self.assertEqual('baz', data['value'])

    def test_cannot_get_other_user_key(self):
        r1 = create_user()
        r2 = create_user()

        id1 = r1.json()['identifier']
        id2 = r2.json()['identifier']

        store_key(id1, key='foo', value='bar')
        response = get_key(id2, key='foo')

        self.assertEqual(404, response.status_code)

    def test_delete_key_for_existing_user_and_key_is_successful(self):
        identifier = create_user().json()['identifier']

        store_key(identifier, key='foo', value='bar')
        response = delete_key(identifier, key='foo')

        self.assertEqual(202, response.status_code)

        response = get_key(identifier, key='foo')
        self.assertEqual(404, response.status_code)

    def test_delete_key_for_non_existing_user_returns_404(self):
        identifier = str(uuid.uuid4())
        response = delete_key(identifier, key='foo')

        self.assertEqual(404, response.status_code)
        self.assertEqual('application/json', response.headers['Content-Type'], 'Content-Type should be application/json')

    def test_delete_non_existing_key_returns_404(self):
        identifier = create_user().json()['identifier']
        response = delete_key(identifier, key='foo')

        self.assertEqual(404, response.status_code)
        self.assertEqual('application/json', response.headers['Content-Type'], 'Content-Type should be application/json')

if __name__ == '__main__':
    unittest.main()
