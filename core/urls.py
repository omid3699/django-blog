from django.contrib import admin
from django.urls import path, include

from posts.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("posts.urls")),
    path("", index),
]