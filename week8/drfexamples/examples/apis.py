from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .authentication import CurlAuthentication


class UniversalTruth(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (CurlAuthentication, )

    def get(self, request):
        return Response({'answer': 42})

    def post(self, request):
        return Response({'answer': 43})
