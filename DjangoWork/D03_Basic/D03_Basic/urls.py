"""D03_Basic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from D03_Basic import views

urlpatterns = [
    # path(url, func)
    # path("admin/", admin.site.urls),

    path('aaa/', views.index),  #  aaa/ 라는 url 로 요청이 오면 views 모듈의 index 함수가 처리

    path('aaa/bbb/ccc/', views.index2),

    path('user/', include('user.urls')),  # user/ ... 로 url 요청이 들어오면 user 앱의 urls.py 가 위임받아 처리 
]
