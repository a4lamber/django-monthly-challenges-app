from django.urls import path

# 导入本文件夹中的views.py
from . import views

urlpatterns = [
    path(route="", view=views.index, name="index"),  # trigger for /challenges/
    path(route="<int:month>", view=views.monthly_challenge_by_number),
    path(route="<str:month>", view=views.monthly_challenge, name="month-challenges"),
]
