import jwt
import datetime
from django.conf import settings

JWT_SECRET_KEY = settings.JWT_SECRET_KEY
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 3600

def create_jwt_token(payload):
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_EXP_DELTA_SECONDS)
    token = jwt.encode(payload, JWT_SECRET_KEY, JWT_ALGORITHM)
    return token

def decode_jwt_token(token):

    try:
        payload1 = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
        print(payload1)
        return payload1
    except jwt.ExpiredSignatureError:
        return 'Token has expired'
    except jwt.InvalidTokenError:
        return 'Invalid token'
# def decode_jwt_token(token):
#     secret_key = settings.JWT_SECRET_KEY
#     try:
#         payload = jwt.decode(token, secret_key, algorithms=['HS256'])
#         return payload
#     except jwt.ExpiredSignatureError:
#         return 'Token has expired'
#     except jwt.InvalidTokenError:
#         return 'Invalid token'
