#store all urls local to this app
from django.urls import path
from django.urls import include
from .views import main
urlpatterns = [
    path("", main),
]
