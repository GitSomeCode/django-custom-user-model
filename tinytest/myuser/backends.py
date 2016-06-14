from django.conf import settings
from django.contrib.auth.hashers import check_password

from .models import User


class EmailAuthBackend(object):
    '''
    A custom authentication backend, allowing users
    to log in with their email address.
    '''

    def authenticate(self, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None

