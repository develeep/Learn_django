from django.contrib import admin
from django.urls import path, include
from posts.views import index, function_view, url_view, url_parameter, class_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', url_view),
    path('url/<str:username>/', url_parameter),
    path('fbv/', function_view),
    path('cbv/', class_view.as_view()),
    path("", index, name='index'),
    path("posts/", include('posts.urls', namespace='posts')),
]
