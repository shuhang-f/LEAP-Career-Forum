from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name = 'logout' ),
    path('signup/', views.signup_view, name = 'signup' ),
    path('home/', views.home_view, name='home'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('landing/', views.facebook_callback, name='facebook_callback'),
]

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'