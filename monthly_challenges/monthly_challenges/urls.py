"""monthly_challenges URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

urlpatterns = [
    path("admin/", admin.site.urls),
    # Step 1: 相当于指路牌, client request中的url, 包括challenges/ 则points to challenges.url中寻找答案
    # Step 2: 在challenges的urls.py，寻找url pattern, 里边包含了 resource name + function/class to call for view
    # Step 3: view相当于返回信息的工具人，可以定义一个string or database call.
    path("challenges/", include("challenges.urls")),
]
