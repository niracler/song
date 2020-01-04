from django.contrib.auth.models import AbstractUser
from django.utils.deprecation import MiddlewareMixin
import jwt


class MyUser(object):
    id = 0
    username = ''
    is_anonymous = True
    is_authenticated = False


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        token = request.headers.get("Token", "")
        try:
            token = jwt.decode(token, 'onlinemusic', algorithms=['HS256'])
            user = MyUser()
            user.id = token['uid']
            user.username = token['name']
            user.is_anonymous = False
            user.is_authenticated = True
            request.myuser = user
        except Exception as e:
            request.myuser = None
