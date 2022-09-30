from django.urls import path,include

urlpatterns = [
    path('user/',include("app.user.urls")),
    path('community/',include("app.community.urls")),
    path('post/',include("app.post.urls")),
]
