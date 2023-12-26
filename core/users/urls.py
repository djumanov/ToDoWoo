from django.urls import path

from .views import SignUpView

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', obtain_auth_token, name='signin'),
]
