from django.urls import path, include
from .views import SigninView, SignupView, ProfileView, signout



urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('signout/', signout, name='signout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='user-profile')
]
