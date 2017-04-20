from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .authentication import CurlAuthentication


class JwtApiAuthentication:
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )


class UniversalTruth(JwtApiAuthentication, APIView):
    def get(self, request):
        return Response({'answer': 42})

    def post(self, request):
        return Response({'answer': 43})
