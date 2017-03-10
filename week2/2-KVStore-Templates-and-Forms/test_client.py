import uuid
import re
import requests
import unittest


UUID4_REGEX = re.compile('([a-zA-Z]|[0-9]){8}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){12}')
BASE_URL = 'http://localhost:8000'

API_BASE = '/api/storage'
CREATE_USER_URL = BASE_URL + API_BASE + '/create-user/'
STORE_KEY_URL = BASE_URL + API_BASE + '/{identifier}/'
GET_KEY_URL = BASE_URL + API_BASE + '/{identifier}/{key}/'
DELETE_KEY_URL = BASE_URL + API_BASE + '/{identifier}/{key}/'

INDEX_VIEW = '/'
USER_DETAIL_VIEW = '/user-detail/{identifier}/'
ADD_KEY_VIEW = '/add-key/{identifier}/'

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


class KeyValueStoreApiTests(unittest.TestCase):
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


class KeyValueHtmlViewsTests(unittest.TestCase):
    def test_index_view_exists(self):
        response = requests.get(BASE_URL + INDEX_VIEW)

        self.assertEqual(200, response.status_code)
        self.assertEqual('text/html; charset=utf-8', response.headers['Content-Type'])

    def test_index_view_contains_desired_elements(self):
        id1 = create_user().json()['identifier']
        id2 = create_user().json()['identifier']

        response = requests.get(BASE_URL + INDEX_VIEW)
        content = response.content.decode('utf-8')

        self.assertIn('<table>', content, 'There should be at least 1 table')
        self.assertIn(id1, content, 'First user should be there')
        self.assertIn(id2, content, 'Second user should be there')
        self.assertIn(USER_DETAIL_VIEW.format(identifier=id1), content, 'There should be a link for user1')
        self.assertIn(USER_DETAIL_VIEW.format(identifier=id2), content, 'There should be a link for user2')


    def test_user_detail_view_exists(self):
        identifier = create_user().json()['identifier']
        response = requests.get(BASE_URL + USER_DETAIL_VIEW.format(identifier=identifier))

        self.assertEqual(200, response.status_code)
        self.assertEqual('text/html; charset=utf-8', response.headers['Content-Type'])

    def test_user_detail_view_contains_desired_elements(self):
        identifier = create_user().json()['identifier']
        k1, v1 = 'name', 'asf'
        k2, v2 = 'foo', 'bar'

        store_key(identifier, key=k1, value=v1)
        store_key(identifier, key=k2, value=v2)

        response = requests.get(BASE_URL + USER_DETAIL_VIEW.format(identifier=identifier))
        content = response.content.decode('utf-8')

        self.assertIn('<table>', content, 'There should be at least 1 table')
        self.assertIn(k1, content, 'Key1 is present')
        self.assertIn(v1, content, 'Value1 is present')

        self.assertIn(k2, content, 'Key2 is present')
        self.assertIn(v2, content, 'Value2 is present')

    def test_user_detail_view_for_non_existing_user_returns_404(self):
        identifier = 'asdf'
        response = requests.get(BASE_URL + USER_DETAIL_VIEW.format(identifier=identifier))

        self.assertEqual(404, response.status_code)

    def test_add_key_view_exists(self):
        identifier = create_user().json()['identifier']
        response = requests.get(BASE_URL + ADD_KEY_VIEW.format(identifier=identifier))

        self.assertEqual(200, response.status_code)
        self.assertEqual('text/html; charset=utf-8', response.headers['Content-Type'])

    def test_add_key_view_contains_desired_elements(self):
        identifier = create_user().json()['identifier']

        response = requests.get(BASE_URL + ADD_KEY_VIEW.format(identifier=identifier))
        content = response.content.decode('utf-8')

        self.assertIn('<form', content, 'There should be form')
        self.assertIn('method="POST"', content, 'Form method should be post')
        self.assertIn('<input', content, 'There should be input')

    def test_add_key_view_for_non_existing_user_returns_404(self):
        identifier = 'asdf'
        response = requests.get(BASE_URL + ADD_KEY_VIEW.format(identifier=identifier))

        self.assertEqual(404, response.status_code)

if __name__ == '__main__':
    unittest.main()
