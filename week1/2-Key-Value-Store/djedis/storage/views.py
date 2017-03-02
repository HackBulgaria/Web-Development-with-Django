import json

from django.http import JsonResponse, HttpResponse

from .services import create_user, set_key, get_key, delete_key
from .exceptions import UserDoesNotExist


def set_key_view(request, identifier):
    body = request.body.decode('utf-8')
    payload = json.loads(body)

    key = payload['key']
    value = payload['value']

    try:
        result = set_key(identifier=identifier, key=key, value=value)
    except UserDoesNotExist:
        error = {
            'error': 'User not found.'
        }
        return JsonResponse(error, status=404)

    return JsonResponse(payload, status=201)


def manage_key_view(request, identifier, key):
    if request.method == 'GET':
        return get_key_view(request, identifier, key)

    if request.method == 'DELETE':
        return delete_key_view(request, identifier, key)

    return HttpResponse(status=405)


def get_key_view(request, identifier, key):
    try:
        value = get_key(identifier=identifier, key=key)
    except UserDoesNotExist:
        error = {
            'error': 'User not found.'
        }
        return JsonResponse(error, status=404)

    if value is None:
        error = {
            'error': 'Key not found.'
        }
        return JsonResponse(error, status=404)

    return JsonResponse({'value': value})


def delete_key_view(request, identifier, key):
    try:
        value = delete_key(identifier=identifier, key=key)
    except UserDoesNotExist:
        error = {
            'error': 'User not found.'
        }
        return JsonResponse(error, status=404)

    if value is None:
        error = {
            'error': 'Key not found.'
        }
        return JsonResponse(error, status=404)

    return JsonResponse({'value': value}, status=202)


def create_user_view(request):
    identifier = create_user()

    return JsonResponse({'identifier': identifier})
