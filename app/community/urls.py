from django.urls import path, include
from .views import JoinCommunityView, MyCommunitiesView,CreateCommunityView

urlpatterns = [
    path('join-community/', JoinCommunityView.as_view(), name='join-community'),
    path('remove-community/', MyCommunitiesView.as_view(), name='remove-community'),
    path('create-community/',CreateCommunityView.as_view(),name='create-community'),
]
