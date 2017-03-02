import os
import uuid
import json

from django.conf import settings

from .exceptions import UserDoesNotExist


def uuid4():
    return str(uuid.uuid4())


def write_user_database(identifier, data):
    identifier_json = identifier + '.json'
    path = os.path.join(settings.JSON_DATABASE_DIR, identifier_json)

    with open(path, 'w') as f:
        f.write(json.dumps(data, indent=4))


def create_user():
    identifier = uuid4()

    write_user_database(identifier, data={})

    return identifier


def get_user_database(identifier):
    identifier_json = identifier + '.json'
    path = os.path.join(settings.JSON_DATABASE_DIR, identifier_json)
    data = {}

    if not os.path.exists(path):
        raise UserDoesNotExist

    with open(path, 'r') as f:
        data = json.loads(f.read())

    return data


def set_key(*, identifier, key, value):
    data = get_user_database(identifier)
    data[key] = value

    write_user_database(identifier, data)

    return data


def get_key(*, identifier, key):
    data = get_user_database(identifier)

    return data.get(key)


def delete_key(*, identifier, key):
    data = get_user_database(identifier)

    if key not in data:
        return None

    value = data.pop(key)

    write_user_database(identifier, data)

    return value
