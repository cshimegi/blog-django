"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from users.urls import routers as UserAPI
from posts.urls import routers as PostAPI

API_BASE_PATH = 'api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(API_BASE_PATH + 'users/', include(UserAPI.urls)),
    path(API_BASE_PATH + 'posts/', include(PostAPI.urls)),
]
