from django.urls import path,include

from .views import HomeView, add_comment,CreatePostView,tag_filter

urlpatterns = [
    path('home/',HomeView.as_view(),name='home'),
    path('add-comment/',add_comment,name='add-comment'),
    path('create-post/',CreatePostView.as_view(),name='create-post'),
    path('tag-filter/<int:id>/',tag_filter,name='tag-filter')
]