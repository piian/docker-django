
from django.contrib import admin

from django.urls import path
from . import views

urlpatterns = [
    path('', include('blogs.urls'), namespace='blogs'),
    path('admin/', admin.site.urls),
]