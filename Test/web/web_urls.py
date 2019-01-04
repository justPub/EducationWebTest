from django.urls import path, include, re_path
from web.views import hello
# app_name = 'hello'
urlpatterns = [
    path('hello/', hello),
]
