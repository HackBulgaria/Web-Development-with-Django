import os
import uuid
import json

from django.conf import settings

from .exceptions import UserDoesNotExist
from .models import User, KeyValue


def write_user_database(identifier, data):
    identifier_json = identifier + '.json'
    path = os.path.join(settings.JSON_DATABASE_DIR, identifier_json)

    with open(path, 'w') as f:
        f.write(json.dumps(data, indent=4))


def create_user():
    user = User.objects.create()

    return str(user.identifier)


def get_user(identifier):
    try:
        user = User.objects.get(identifier=identifier)
    except User.DoesNotExist:
        raise UserDoesNotExist

    return user


def set_key(*, identifier, key, value):
    user = get_user(identifier)

    try:
        kv = user.data.get(key=key)
        kv.value = value
        kv.save()
    except KeyValue.DoesNotExist:
        kv = KeyValue.objects.create(user=user, key=key, value=value)

    return kv


def get_key(*, identifier, key):
    user = get_user(identifier)

    return user.data.filter(key=key).first()


def delete_key(*, identifier, key):
    kv = get_key(identifier=identifier, key=key)

    if kv is None:
        return None

    kv.delete()

    return kv.value
