from django.contrib.auth.models import AbstractUser
from django.utils.deprecation import MiddlewareMixin
import jwt


class User(AbstractUser):
    is_anonymous = True
    is_authenticated = False


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        token = request.headers.get("Token", "")
        try:
            token = jwt.decode(token, 'onlinemusic', algorithms=['HS256'])
            user = User()
            user.id = token['uid']
            user.is_anonymous = False
            user.is_authenticated = True
            request.myuser = user
        except Exception as e:
            print(e)
            user = User()
            user.id = -1
            user.is_anonymous = True
            user.is_authenticated = False
            request.myuser = user

        print("我也就你进来的时候打个招呼")