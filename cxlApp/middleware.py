from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
import jwt
from cxlApp.auth import decode_jwt_token
from django.conf import settings
from cxlApp.views import login_view
from django.contrib.auth import get_user_model

User = get_user_model

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        #print("Request Headers:", request.META)
        login_view(request)
        
        token = request.META.get('HTTP_AUTHORIZATION')
        #print("Authorization Header:", token)  # Debug print statement

        if token:
            payload = decode_jwt_token(token)
            request.user_payload = payload
        else:
            request.user_payload = None
        
        response = self.get_response(request)
        return response
# import jwt
# from django.http import JsonResponse
# from django.conf import settings

# class JWTAuthenticationMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Get the token from the Authorization header
#         token = request.META.get('HTTP_AUTHORIZATION')
#         if token is not None:
#             try:
#                 # Verify the token
#                 payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
#                 # Attach the payload to the request object
#                 request.user_payload = payload
           
