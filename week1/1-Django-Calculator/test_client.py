import requests


BASE_URL = 'http://localhost:8000'

TESTS = [
    ('/calculator/add/1/2/', 3),
    ('/calculator/add/1/1/', 2),
    ('/calculator/add/0/0/', 0),
    ('/calculator/add/1000/3/', 1003),
    ('/calculator/multiply/1/2/', 2),
    ('/calculator/multiply/1/1/', 1),
    ('/calculator/multiply/0/0/', 0),
    ('/calculator/multiply/1000/3/', 3000),
    ('/calculator/power/1/2/', 1),
    ('/calculator/power/2/1/', 2),
    ('/calculator/power/2/0/', 1),
    ('/calculator/power/1000/3/', 1000000000),
    ('/calculator/fact/1/', 1),
    ('/calculator/fact/2/', 2),
    ('/calculator/fact/0/', 1),
    ('/calculator/fact/5/', 120),
    ('/calculator/fact/20/', 2432902008176640000),
]


def run(url, expected):
    print('Running against {}'.format(url))

    response = requests.get(url, timeout=1)
    result = int(response.text)

    if expected != result:
        raise AssertionError('Called {}. Expected {}, got {}'.format(url, expected, result))

    print('OK')


def run_json(url, expected):
    url = url + '?format=json'
    print('Running against {}'.format(url))

    response = requests.get(url, timeout=1)
    content_type = response.headers['Content-Type']

    if content_type != 'application/json':
        raise AssertionError('Expected application/json, got {}'.format(content_type))

    result = response.json()

    if expected != result['result']:
        raise AssertionError('Called {}. Expected {}, got {}'.format(url, expected, result))

    print('OK')


def main():
    for url, expected in TESTS:
        run(BASE_URL + url, expected)
        run_json(BASE_URL + url, expected)


if __name__ == '__main__':
    main()
