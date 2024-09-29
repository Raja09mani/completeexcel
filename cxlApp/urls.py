from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cxlApp.views import StudentDetailViewSet, StudentMarkViewSet, get_view
from cxlApp.views import update_database, update_database_header, call_api_view, api_view, login_view, protected_view ,test

router = DefaultRouter()
router.register(r'students', StudentDetailViewSet)
router.register(r'marks', StudentMarkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('update_database/', update_database, name='update_database'),
    path('update_database_header/', update_database_header, name='update_database_header'),
    path('call-api/', call_api_view, name='call_api_view'),
    path('weather-api/', api_view, name='api_view'),
    path('login_view/', login_view, name='login_view'),
    path('protected/', protected_view, name='protected_view'),
    path('test/', test, name='test'),
]
